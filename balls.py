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
#bg = pygame.image.load("sn2000.png")
bg = None
pitch = 0

screen = pygame.display.set_mode(size, flags = 0, vsync = 1)

ball = pygame.image.load("starship.png")


# Halve ship size
ballrect = ball.get_rect()
ballrect[2] = ballrect[2] / 2
ballrect[3] = ballrect[3] / 2
ballsize = (ballrect[2], ballrect[3])
ball = pygame.transform.scale(ball, ballsize)


while 1:
    pitch_rad = pitch * math.pi / 180
    thrust_vector = (-math.sin(pitch_rad) / thrust, -math.cos(pitch_rad) / thrust)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        speed = vec_add(speed, thrust_vector)
    if keys[pygame.K_DOWN]:
        speed = vec_sub(speed, thrust_vector)
    if  keys[pygame.K_LEFT]:
        pitch = pitch + 2
    if  keys[pygame.K_RIGHT]:
        pitch = pitch - 2
        
           
    ball_rotated = pygame.transform.rotate(ball, pitch)        

    # Add gravity
    speed = vec_add(speed, grav)

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    if bg is None:
        screen.fill(black)
    else:
        screen.blit(bg, (0, 0))
    screen.blit(ball_rotated, ballrect)
    pygame.display.flip()
    time.sleep(0.0)
    print(f"speed={speed} thrustvector={thrust_vector}")

