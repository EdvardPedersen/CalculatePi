"""
This application calculates pi using a monte carlo method,
and visualizes the results compared to the constant in the
math library
"""

from random import random
from math import sqrt
from math import pi
from collections import deque
from time import clock

import pygame

def calculate_pi(iterations):
    """
    Calculates pi using a monte carlo method, returns pi

    As the are of a circle is pi * r ^ 2, and the area of
    a square is (2 * r) ^ 2, we can calculate pi by estimating
    the ratio between points inside a circle and a square where
    the circle fits perfectly inside the square.
    When this ratio is multiplied by 4, the result is pi.

    Arguments:
    iterations -- the number of random points generated
    """
    # TODO: Replace with an iterator?
    points_inside = 0
    for _ in range(iterations):
        # Generate a random point between (-0.5, -0.5) and (0.5, 0.5)
        x_position = random() - 0.5
        y_position = random() - 0.5
        # Check if point is inside the circle
        if sqrt(x_position**2 + y_position**2) <= 0.5:
            points_inside += 1
    estimated_pi = 4 * points_inside / iterations
    return estimated_pi



class PiEstimation:
    """
    Class for visualizing and calculating pi
    """
    def __init__(self):
        """
        Sets up pygame, and variables used for visualization
        DO NOT MODIFY
        """
        # Pygame initialization
        pygame.init()
        self.screen = pygame.display.set_mode((800, 800))
        self.point = pygame.Surface((1, 5))
        self.point.fill((0, 255, 0))

        # Variables used for visualization
        self.accumulated_error = 0
        self.values = deque(maxlen=800)
        self.time_iteration = clock()

        # Calculated pi for the current number of iterations
        self.current_iterations = 100
        self.current_pi = 0

    def mainloop(self):
        '''
        Continously calculates a more correct value for pi
        and draws this on screen, loops forever.
        '''
        # TODO: Change to use an iterator?
        while True:
            self.current_pi = calculate_pi(self.current_iterations)
            self.current_iterations += 1
            self._draw_screen()

    def _draw_screen(self):
        """
        Draws the last 800 estimated values for pi, as well as
        the reference from math.pi
        DO NOT MODIFY
        """
        # Clear screen
        self.screen.fill((0, 0, 0))
        self.accumulated_error += abs(self.current_pi - pi)

        # Add most current 
        self.values.append(self._pi2y(self.current_pi))

        # Draw all estimates on the screen
        for x_position, y_position in enumerate(self.values):
            self.screen.blit(self.point, (x_position, y_position))

        # Draw the reference pi value on the screen
        pygame.draw.line(self.screen, (255, 0, 0), (750, self._pi2y(pi)), (800, self._pi2y(pi)), 3)
        pygame.display.flip()

        # Print statistics every 100 iterations
        if self.current_iterations % 100 == 0:
            time_passed = clock() - self.time_iteration
            output = "At iteration {:>6}, average error is {:<8.5}, " \
                     "done in {:<4.2} seconds ({} FPS)"
            print(output.format(self.current_iterations,
                                self.accumulated_error/100,
                                time_passed,
                                int(100/time_passed)))
            self.accumulated_error = 0
            self.time_iteration = clock()

    def _pi2y(self, value):
        # Do not modify this method
        return int((value - 2.5) * 600)

if __name__ == "__main__":
    estimator = PiEstimation()
    estimator.mainloop()
