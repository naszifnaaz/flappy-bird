# This is my attempt at re-creating the iconic flappy bird game which took the internet by storm in early 2013.
import pygame
import sys
from setup.constants import *

# Pygame Initialisation
pygame.init()
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Flappy Bird")
gameicon = pygame.image.load('assets/scene/gameicon.png').convert_alpha()
pygame.display.set_icon(gameicon)
clock = pygame.time.Clock()

# Rendering game scene
background_scene = pygame.image.load('assets/scene/background.png').convert()
background_scene = pygame.transform.scale(background_scene, (width, height))
floor_scene = pygame.image.load('assets/scene/floor.png').convert()
floor_scene = pygame.transform.scale2x(floor_scene)
win.blit(background_scene, (0, 0))
win.blit(floor_scene, (0, 670))

while run:
    # setting up game events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    clock.tick(fps)
