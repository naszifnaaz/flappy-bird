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

# Loading bird sprites
bird_sprite = pygame.image.load('assets/sprites/bird_mid.png').convert()
bird_sprite = pygame.transform.scale2x(bird_sprite)
bird_hitbox = bird_sprite.get_rect(center=(100, 400))

# Drawing pipe obstacles
pipe_sprite = pygame.image.load('assets/sprites/pipe.png').convert()
pipe_sprite = pygame.transform.scale2x(pipe_sprite)
pipe_list = []
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1200)


# Drawing dynamic floor
def draw_floor():
    win.blit(floor_scene, (dynamic_floor, 700))
    win.blit(floor_scene, (dynamic_floor + 500, 700))


# Drawing new pipe
def create_pipe():
    new_pipe = pipe_sprite.get_rect(midtop=(700, 400))
    return new_pipe


# Dynamic obstacles
def move_pipe(pipes):
    for pipe in pipes:
        pipe.centerx -= 5
    return pipes


# Rendering pipes
def draw_pipe(pipes):
    for pipe in pipes:
        win.blit(pipe_sprite, pipe)


# Game loop
while run:
    # setting up game events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_velocity = 0
                bird_velocity -= 10

        if event.type == SPAWNPIPE:
            pipe_list.append(create_pipe())

    win.blit(background_scene, (0, 0))

    # implementing bird physics
    bird_velocity += gravity
    bird_hitbox.centery += bird_velocity
    win.blit(bird_sprite, bird_hitbox)

    # rendering obstacles
    pipe_list = move_pipe(pipe_list)
    draw_pipe(pipe_list)

    # dynamic floor
    dynamic_floor -= 1
    draw_floor()
    if dynamic_floor <= -500:
        dynamic_floor = 0

    pygame.display.update()
    clock.tick(fps)
