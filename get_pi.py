from random import random
from math import sqrt
from math import pi
from collections import deque
from time import clock

import pygame

def calculate_pi(iterations):
    points_inside = 0
    points_outside = 0
    for _ in range(iterations):
        x = random() - 0.5
        y = random() - 0.5
        if(sqrt(x**2 + y**2) > 0.5):
            points_outside += 1
        else:
            points_inside += 1
    return (4*points_inside /( points_outside + points_inside))


# Pygame setup
pygame.init()
screen = pygame.display.set_mode((800,800))

# Variables used in loop
current_iterations = 100
accumulated_error = 0
values = deque()

# Setup points
point = pygame.Surface((1,5))
point.fill((0,255,0))

# Setup timer
time_iteration = clock()

# Get y value based on pi value
def pi2y(value):
    return int((value-2.5)*600)

while(True):
    # Calculate pi
    current_pi = calculate_pi(current_iterations)
    current_iterations += 1

    screen.fill((0,0,0))
    current_error = abs(current_pi - pi)
    current_y = pi2y(current_pi)
    values.append(current_y)
    if len(values) > 799:
        values.popleft()
    for x, y in enumerate(values):
        screen.blit(point,(x,y))
    pygame.draw.line(screen,(255,0,0), (750, pi2y(pi)), (800, pi2y(pi)), 10)
    pygame.display.flip()
    accumulated_error += current_error
    if current_iterations % 100 == 0:
        time_passed = clock() - time_iteration
        print("At iteration {}, average error is {}, done in {} seconds".format(current_iterations, accumulated_error/100, time_passed))
        accumulated_error = 0
        time_iteration = clock()
