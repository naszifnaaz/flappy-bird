# This is my attempt at re-creating the iconic flappy bird game which took the internet by storm in early 2013.
import pygame
import sys
from setup.constants import *
import random

# Pygame Initialisation
pygame.init()
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")
gameicon = pygame.image.load('assets/scene/gameicon.png').convert_alpha()
pygame.display.set_icon(gameicon)
clock = pygame.time.Clock()

# Rendering game scene
background_scene = pygame.image.load('assets/scene/background.png').convert()
background_scene = pygame.transform.scale(background_scene, (WIDTH, HEIGHT))
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
pipe_height = [200, 400, 550]
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1500)


# Drawing dynamic floor
def draw_floor():
    win.blit(floor_scene, (DYNAMIC_FLOOR, 700))
    win.blit(floor_scene, (DYNAMIC_FLOOR + 500, 700))


# Drawing new pipe
def create_pipe():
    random_pipe = random.choice(pipe_height)
    bottom_pipe = pipe_sprite.get_rect(midtop=(700, random_pipe))
    top_pipe = pipe_sprite.get_rect(midbottom=(700, random_pipe - 250))
    return bottom_pipe, top_pipe


# Dynamic obstacles
def move_pipe(pipes):
    for pipe in pipes:
        pipe.centerx -= 5
    return pipes


# Rendering pipes
def draw_pipe(pipes):
    for pipe in pipes:
        if pipe.bottom >= 800:
            win.blit(pipe_sprite, pipe)
        else:
            flip_pipe = pygame.transform.flip(pipe_sprite, False, True)
            win.blit(flip_pipe, pipe)


# Collision detection
def check_collision(pipes):
    for pipe in pipes:
        if bird_hitbox.colliderect(pipe):
            return False
    if bird_hitbox.top <= -100 or bird_hitbox.bottom >= 700:
        return False
    return True


# Game loop
while RUN:
    # setting up game events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and GAME_ACTIVE == True:
                BIRD_VELOCITY = 0
                BIRD_VELOCITY -= 8

            if event.key == pygame.K_SPACE and GAME_ACTIVE == False:
                GAME_ACTIVE = True
                pipe_list.clear()
                bird_hitbox.center = (100, 400)
                BIRD_VELOCITY = 0

        if event.type == SPAWNPIPE:
            pipe_list.extend(create_pipe())

    win.blit(background_scene, (0, 0))

    if GAME_ACTIVE:

        # implementing bird physics
        BIRD_VELOCITY += GRAVITY
        bird_hitbox.centery += BIRD_VELOCITY
        win.blit(bird_sprite, bird_hitbox)
        GAME_ACTIVE = check_collision(pipe_list)

        # rendering obstacles
        pipe_list = move_pipe(pipe_list)
        draw_pipe(pipe_list)

    # dynamic floor
    DYNAMIC_FLOOR -= 1
    draw_floor()
    if DYNAMIC_FLOOR <= -500:
        DYNAMIC_FLOOR = 0

    pygame.display.update()
    clock.tick(FPS)
