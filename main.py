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

# Quit the game if the user clicks the close button (GAME OVER)
app_running = True
while app_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            app_running = False


