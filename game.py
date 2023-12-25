import pygame
import random

# constants
WINDOW_SIZE = 200
SNAKE_SIZE = 10
GREEN = (204, 255, 204)
RED = (255, 204, 204)
BLACK = (0, 0, 0)

# initialize
running  = True
snake = [(WINDOW_SIZE // 2, WINDOW_SIZE // 2)]
direction = [0, 0]  # x, y
food = (random.randint(0, (WINDOW_SIZE - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE,
        random.randint(0, (WINDOW_SIZE - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE)

pygame.init()
window = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption('snake')
clock = pygame.time.Clock()

def move(arrow):
    global direction
    if arrow == "left":
        direction = [-SNAKE_SIZE, 0]
    elif arrow == "right":
        direction = [SNAKE_SIZE, 0]
    elif arrow == "up":
        direction = [0, -SNAKE_SIZE]
    elif arrow == "down":
        direction = [0, SNAKE_SIZE]

def wrap_around(head):
    if head[0] >= WINDOW_SIZE:
        head = (0, head[1])
    elif head[0] < 0:
        head = (WINDOW_SIZE - SNAKE_SIZE, head[1])
    if head[1] >= WINDOW_SIZE:
        head = (head[0], 0)
    elif head[1] < 0:
        head = (head[0], WINDOW_SIZE - SNAKE_SIZE)
    return head

def update_snake():
    global food
    head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
    head = wrap_around(head)
    snake.insert(0, head)
    if snake[0] == food:
        food = (random.randint(0, (WINDOW_SIZE - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE,
                random.randint(0, (WINDOW_SIZE - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE)
    else:
        snake.pop()

def draw_snake(food):
    window.fill(BLACK)
    for square in snake:
        pygame.draw.rect(window, GREEN, (int(square[0]), int(square[1]), SNAKE_SIZE, SNAKE_SIZE))
    pygame.draw.rect(window, RED, (int(food[0]), int(food[1]), SNAKE_SIZE, SNAKE_SIZE))
    pygame.display.flip()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                move("up")
            elif event.key == pygame.K_DOWN:
                move("down")
            elif event.key == pygame.K_LEFT:
                move("left")
            elif event.key == pygame.K_RIGHT:
                move("right")
    
    update_snake()
    if snake[0] in snake[1:]:
        running = False

    draw_snake(food)
    clock.tick(10)