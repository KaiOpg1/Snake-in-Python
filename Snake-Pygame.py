import pygame
import random
import sys

# Initialisierung
pygame.init()

# Bildschirmgröße
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Farben
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
WHITE = (255, 255, 255)

# Snake und Food
snake = [(100, 100), (90, 100), (80, 100)]
snake_direction = "RIGHT"
food = (300, 200)

# Clock
clock = pygame.time.Clock()
score = 0

def draw_snake(snake):
    for x, y in snake:
        pygame.draw.rect(screen, GREEN, (x, y, CELL_SIZE, CELL_SIZE))

def draw_food(position):
    pygame.draw.rect(screen, RED, (position[0], position[1], CELL_SIZE, CELL_SIZE))

def game_over():
    font = pygame.font.SysFont("Arial", 35)
    text = font.render("Game Over! Score: " + str(score), True, WHITE)
    screen.blit(text, (WIDTH // 6, HEIGHT // 3))
    pygame.display.flip()
    pygame.time.wait(2000)
    pygame.quit()
    sys.exit()

# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != "DOWN":
                snake_direction = "UP"
            elif event.key == pygame.K_DOWN and snake_direction != "UP":
                snake_direction = "DOWN"
            elif event.key == pygame.K_LEFT and snake_direction != "RIGHT":
                snake_direction = "LEFT"
            elif event.key == pygame.K_RIGHT and snake_direction != "LEFT":
                snake_direction = "RIGHT"

    # Snake Bewegung
    x, y = snake[0]
    if snake_direction == "UP":
        y -= CELL_SIZE
    elif snake_direction == "DOWN":
        y += CELL_SIZE
    elif snake_direction == "LEFT":
        x -= CELL_SIZE
    elif snake_direction == "RIGHT":
        x += CELL_SIZE
    new_head = (x, y)

    # Kollisionen prüfen
    if (x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT or new_head in snake):
        game_over()

    snake.insert(0, new_head)

    # Essen checken
    if new_head == food:
        score += 1
        food = (random.randrange(0, WIDTH // CELL_SIZE) * CELL_SIZE,
                random.randrange(0, HEIGHT // CELL_SIZE) * CELL_SIZE)
    else:
        snake.pop()

    # Bildschirm zeichnen
    screen.fill(BLACK)
    draw_snake(snake)
    draw_food(food)

    font = pygame.font.SysFont("Arial", 20)
    score_text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(10)
