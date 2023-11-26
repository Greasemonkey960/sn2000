#!/usr/bin/python3

import sys, pygame
import time
import math

pygame.init()

def vec_add(a, b):
    r = [a[0] + b[0], a[1] + b[1]]
    return r

def vec_sub(a, b):
    r = [a[0] - b[0], a[1] - b[1]]
    return r


size = width, height = 1910, 900
speed = [2.7, 0]
thrust = 1.0
grav = [0, 0.2]
black = (0, 0, 0)
bg = pygame.image.load("sn2000.png")
pitch = 0

screen = pygame.display.set_mode(size, flags = pygame.DOUBLEBUF | pygame.SCALED, vsync = 1)

ship = pygame.image.load("starship.png")
explosion = pygame.image.load("nuclear-explosion.png")
exploded = False


# Halve ship size
shiprect = ship.get_rect()
shiprect[2] = shiprect[2] / 2
shiprect[3] = shiprect[3] / 2
ballsize = (shiprect[2], shiprect[3])
ship = pygame.transform.scale(ship, ballsize)
explosion = pygame.transform.scale(explosion, ballsize)


while True:
    pitch_rad = pitch * math.pi / 180
    thrust_vector = (-math.sin(pitch_rad) * thrust, -math.cos(pitch_rad) * thrust)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and not exploded:
        speed = vec_add(speed, thrust_vector)
    #if keys[pygame.K_DOWN]:
    #    speed = vec_sub(speed, thrust_vector)
    if keys[pygame.K_LEFT]:
        pitch = pitch + 2
    if keys[pygame.K_RIGHT]:
        pitch = pitch - 2
    if keys[pygame.K_ESCAPE]:
        # Reset game
        exploded = False
        speed = [0.27, 0]
        shiprect.left = 0
        shiprect.top = 0


    if exploded:
        ship_rotated = explosion
    else:
        ship_rotated = pygame.transform.rotate(ship, pitch)

        # Add gravity
        speed = vec_add(speed, grav)

    shiprect = shiprect.move(speed)
    if shiprect.left < 0 or shiprect.right > width:
        speed[0] = -speed[0]
    if shiprect.top < 0:
        speed[1] = -speed[1]
    if shiprect.bottom > height and not exploded:
        speed[0] = 0
        speed[1] = 0
        exploded = True

    if bg is None:
        screen.fill(black)
    else:
        screen.blit(bg, (0, 0))
    screen.blit(ship_rotated, shiprect)
    pygame.display.flip()
    print(f"speed={speed[0]:.3f} thrustvector={thrust_vector}")

