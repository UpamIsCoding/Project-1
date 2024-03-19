import pygame
import time
import random

# Initialize Pygame
pygame.init()

# Define colors
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Set display dimensions
display_width = 800
display_height = 600

# Set size of snake block
block_size = 20

# Set speed of snake
speed = 20

# Set font
font_style = pygame.font.SysFont(None, 50)

# Set display
game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()

# Define snake
def snake(block_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(game_display, black, [x[0], x[1], block_size, block_size])

# Define message
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    game_display.blit(mesg, [display_width / 6, display_height / 3])

# Main game loop
def gameLoop():
    game_over = False
    game_close = False

    # Set initial position and direction of snake
    lead_x = display_width / 2
    lead_y = display_height / 2
    lead_x_change = 0
    lead_y_change = 0

    snake_list = []
    snake_length = 1

    # Set initial position of food
    food_x = round(random.randrange(0, display_width - block_size) / block_size) * block_size
    food_y = round(random.randrange(0, display_height - block_size) / block_size) * block_size

    while not game_over:

        while game_close == True:
            game_display.fill(white)
            message("You Lost! Press C-Play Again or Q-Quit", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    lead_y_change = block_size
                    lead_x_change = 0

        if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
            game_close = True

        lead_x += lead_x_change
        lead_y += lead_y_change

        game_display.fill(blue)
        pygame.draw.rect(game_display, green, [food_x, food_y, block_size, block_size])

        snake_head = []
        snake_head.append(lead_x)
        snake_head.append(lead_y)
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        snake(block_size, snake_list)

        pygame.display.update()

        if lead_x == food_x and lead_y == food_y:
            food_x = round(random.randrange(0, display_width - block_size) / block_size) * block_size
            food_y = round(random.randrange(0, display_height - block_size) / block_size) * block_size
            snake_length += 1

        clock.tick(speed)

    pygame.quit()
    quit()

gameLoop()
