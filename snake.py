import pygame
import random

# Initialize the pygame library
pygame.init()

# Set the screen size and frame rate
SCREEN_SIZE = (600, 600)
FRAME_RATE = 10

# Create the game screen
screen = pygame.display.set_mode(SCREEN_SIZE)

# Set the game title
pygame.display.set_caption("Snake")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Create the snake as a list of rectangles
snake_body = [pygame.Rect(100, 100, 10, 10), pygame.Rect(90, 100, 10, 10), pygame.Rect(80, 100, 10, 10)]

# Create the food
food = pygame.Rect(random.randint(0, SCREEN_SIZE[0]), random.randint(0, SCREEN_SIZE[1]), 10, 10)

# Initialize the game clock
clock = pygame.time.Clock()

# Set the initial direction of the snake
direction = "RIGHT"

# Main game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            # Change direction based on key pressed
            if event.key == pygame.K_UP:
                direction = "UP"
            elif event.key == pygame.K_DOWN:
                direction = "DOWN"
            elif event.key == pygame.K_LEFT:
                direction = "LEFT"
            elif event.key == pygame.K_RIGHT:
                direction = "RIGHT"
            elif event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()

    # Update the snake's position based on its direction
    if direction == "UP":
        snake_body[0].y -= 10
    elif direction == "DOWN":
        snake_body[0].y += 10
    elif direction == "LEFT":
        snake_body[0].x -= 10
    elif direction == "RIGHT":
        snake_body[0].x += 10

    # Check if the snake has eaten the food
    if snake_body[0].colliderect(food):
        # Increase the size of the snake
        snake_body.append(pygame.Rect(snake_body[-1].x, snake_body[-1].y, 10, 10))
        # Generate new food
        food = pygame.Rect(random.randint(0, SCREEN_SIZE[0]), random.randint(0, SCREEN_SIZE[1]), 10, 10)

    # Check if the snake has hit the borders or itself
    if snake_body[0].x < 0 or snake_body[0].x > SCREEN_SIZE[0] or snake_body[0].y < 0 or snake_body[0].y > SCREEN_SIZE[1]:
        pygame.quit()
        exit()
    for i in range(1, len(snake_body)):
        if snake_body[0].colliderect(snake_body[i]):
            pygame.quit()
            exit()
    
    # Move the snake
    for i in range(len(snake_body) - 1, 0, -1):
        snake_body[i].x = snake_body[i - 1].x
        snake_body[i].y = snake_body[i - 1].y

    # Draw the screen
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, food)
    for rect in snake_body:
        pygame.draw.rect(screen, WHITE, rect)

    # Update the display
    pygame.display.update()

    # Tick the clock
    clock.tick(FRAME_RATE)

# Quit the game
pygame.quit()


