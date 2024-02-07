import pygame
import random


class Obstacle:
    def __init__(self, screen, width, height, size):
        self.screen = screen
        self.position = (random.randint(0, width - size),
                         random.randint(0, height - size))
        self.size = size

    def draw(self):
        pygame.draw.rect(self.screen, (139, 69, 19),
                         (self.position[0], self.position[1], self.size, self.size))
