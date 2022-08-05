# Space Invaders Game
# By: Adrian Adewunmi
# Date: 28/07/2022
# Version: 1.0
# Description: This is the main file for the Space Invaders game.
#             It contains the main game loop and the main game functions.
#             It also contains the main menu and the game over screen.
#             It also contains the high score screen.
#             It also contains the pause screen.
#             It also contains the game over screen.
# Adapted from: https://www.youtube.com/watch?v=FfWpgLFMI7w
#               https://github.com/attreyabhatt/Space-Invaders-Pygame

import pygame

# Initialize Pygame
pygame.init()

# Set the width and height of the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Changing the Title and Icon of the Game
pygame.display.set_caption('Space Invaders')
icon = pygame.image.load('images/ufo.png')
pygame.display.set_icon(icon)

# Adding Player Image Into The Game
player_img = pygame.image.load('images/player.png')
# Player Image Position
playerX = 370
playerY = 480


# Function to draw the player on the screen
def player(x, y):
    screen.blit(player_img, (x, y))


# Logic for running the game
app_running = True
while app_running:
    # Change the background color
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            app_running = False
        # Keyboard Input
        # If the keystroke is pressed, the player will move left or right
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print('Left Arrow Pressed')
            if event.key == pygame.K_RIGHT:
                print('Right Arrow Pressed')
    # Draw the player on the screen
    player(playerX, playerY)
    pygame.display.update()
