import pygame
import math
import random
import tkinter as tk
from tkinter import messagebox

pygame.init()

screen = pygame.display.set_mode((400, 400))

clock = pygame.time.Clock()

pygame.display.set_caption("Snake Game")

icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

pygame.mixer.music.load('background.mp3')
pygame.mixer.music.play(-1)

font = pygame.font.SysFont("comincansms", 28)

background = pygame.image.load('background.png')

block_size = 20
score_value = 0
body_x = 0
body_y = 0
snake_x = random.randint(20, 380)
snake_y = random.randint(20, 380)
snake_xchange = 0
snake_ychange = 0
food_x = random.randint(30, 350)
food_y = random.randint(30, 350)
gameover = False


def show_score():
    score = font.render("Score:" + str(score_value), True, (255, 255, 255))
    screen.blit(score, (10, 10))


def snake(screen, snake_list):
    for x, y in snake_list:
        pygame.draw.rect(screen, (0, 0, 0), [round(x), round(y), round(block_size), round(block_size)])


def food(x, y):
    rect2 = pygame.Rect(round(x), round(y), round(block_size), round(block_size))
    pygame.draw.rect(screen, (255, 0, 0), rect2, )


def isCollision(food_x, food_y, snake_x, snake_y):
    distance = math.sqrt(math.pow((food_x - snake_x), 2) + math.pow((food_y - snake_y), 2))
    if distance < 21:
        return True
    else:
        return False


def message_box(subject, content):
    root = tk.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    messagebox.showinfo(subject, content)
    try:
        root.destroy()
    except:
        pass


snake_list = []
snake_length = 1

running = True
while running:
    screen.fill((255, 255, 255))
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake_ychange = -5
                snake_xchange = 0
            if event.key == pygame.K_DOWN:
                snake_ychange = 5
                snake_xchange = 0
            if event.key == pygame.K_RIGHT:
                snake_xchange = 5
                snake_ychange = 0
            if event.key == pygame.K_LEFT:
                snake_xchange = -5
                snake_ychange = 0

    snake_x = snake_x + snake_xchange
    snake_y = snake_y + snake_ychange

    if snake_x > 380:
        snake_x = 0
    elif snake_x <= 0:
        snake_x = 380
    if snake_y > 380:
        snake_y = 0
    elif snake_y <= 0:
        snake_y = 380

    show_score()

    collision = isCollision(food_x, food_y, snake_x, snake_y)
    if collision:
        score_value = score_value + 1
        food_x = random.randint(30, 350)
        food_y = random.randint(30, 350)
        snake_length += 5
    food(food_x, food_y)

    head = [snake_x, snake_y]
    snake_list.append(head)

    if len(snake_list) > snake_length:
        del snake_list[0]

    if head in snake_list[:-1]:
        gameover = True

    if gameover:
        message_box('You Lost!!', "PLAY AGAIN....")
        pygame.quit()

    snake(screen, snake_list)
    pygame.display.update()
    clock.tick(60)
