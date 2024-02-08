import pygame
import random

# Colores
RED = (255, 0, 0)


class Food:
    def __init__(self, screen, screen_width, screen_height, segment_size):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.segment_size = segment_size
        self.position = self._get_random_position()

    def _get_random_position(self):
        x = random.randint(0, (self.screen_width - self.segment_size) //
                           self.segment_size) * self.segment_size
        y = random.randint(0, (self.screen_height - self.segment_size) //
                           self.segment_size) * self.segment_size
        return (x, y)

    def draw(self):
        # Calcula el centro del círculo basado en la posición actual
        center = (self.position[0] + self.segment_size //
                  2, self.position[1] + self.segment_size // 2)
        # Dibuja un círculo en lugar de un rectángulo
        pygame.draw.circle(self.screen, RED, center, self.segment_size // 2)

    def respawn(self):
        self.position = self._get_random_position()
