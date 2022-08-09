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
import random

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

# Set Background Image
background = pygame.image.load('images/background.png')

# Adding Player Image Into The Game
player_img = pygame.image.load('images/player.png')
# Player Image Position
playerX = 370
playerY = 480
playerX_change = 0

# Adding Enemy Image Into The Game
enemy_img = pygame.image.load('images/enemy.png')
# Enemy Image Position
enemyX = random.randint(0, 736)
enemyY = random.randint(0, 150)
enemyX_change = random.randint(0, 5)
enemyY_change = random.randint(0, 50)

# Adding Bullet image into the Game
bullet_img = pygame.image.load('images/bullet.png')
# Bullet Image Position
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
# Ready - You can't see the bullet on the screen
bullet_state = 'ready'


# Function to draw the player on the screen
def player(x, y):
    screen.blit(player_img, (x, y))


# Function to draw the enemy on the screen
def enemy(x, y):
    screen.blit(enemy_img, (x, y))


# Function to draw the bullet on the screen
def fire_bullet(x, y):
    global bullet_state
    # Fire - The bullet is currently moving
    bullet_state = 'fire'
    screen.blit(bullet_img, (x + 16, y + 10))


# Logic for running the game
app_running = True
while app_running:
    # Change the background color
    screen.fill((0, 0, 0))
    # Draw the background image
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            app_running = False
        # Player Movement
        # Keyboard Input
        # If the keystroke is pressed down, the player will move left or right
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -2.5
            if event.key == pygame.K_RIGHT:
                playerX_change = 2.5
            # When space is pressed, the bullet will be fired
            if event.key == pygame.K_SPACE:
                fire_bullet(playerX, bulletY)
        # If the keystroke is released, the player will stop moving
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
    # PlayerX Movement
    playerX += playerX_change
    # Player Boundaries
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    # Enemy Movement
    enemyX += enemyX_change
    # Enemy Boundaries
    if enemyX <= 0:
        enemyX_change = 1.5
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = -1.5
        enemyY += enemyY_change
    # Bullet Movement
    if bullet_state == 'fire':
        fire_bullet(playerX, bulletY)
        bulletY -= bulletY_change
    # Draw the player on the screen
    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()
