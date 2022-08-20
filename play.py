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

while run:
    # setting up game events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    clock.tick(fps)
