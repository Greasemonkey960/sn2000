#!/usr/bin/python3

import sys, pygame
import time
pygame.init()

def vec_add(a, b):
    r = [a[0] + b[0], a[1] + b[1]]
    return r

def vec_sub(a, b):
    r = [a[0] - b[0], a[1] - b[1]]
    return r


size = width, height = 1920, 1080
speed = [2.7, 0]
thrust = [0, -1.0]
grav = [0, 0.1]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("starship.png")

# Halve ship size
ballrect = ball.get_rect()
ballrect[2] = ballrect[2] / 2
ballrect[3] = ballrect[3] / 2
ballsize = (ballrect[2], ballrect[3])
ball = pygame.transform.scale(ball, ballsize)


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    if pygame.key.get_pressed()[pygame.K_UP]:
        speed = vec_add(speed, thrust)
    if pygame.key.get_pressed()[pygame.K_DOWN]:
        speed = vec_sub(speed, thrust)
        

    # Add gravity
    speed = vec_add(speed, grav)

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()
    time.sleep(0.01)
    print(f"speed={speed}")

