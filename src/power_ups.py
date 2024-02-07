import pygame
import random


class PowerUp:
    def __init__(self, screen, width, height, size):
        self.screen = screen
        self.width = width
        self.height = height
        self.size = size
        self.type = random.choice(['speed', 'slow', 'invulnerable'])
        self.position = (random.randint(0, width - size),
                         random.randint(0, height - size))
        self.active = True  # El power-up está activo y puede ser recogido

    def draw(self):
        # Dibuja el power-up basado en su tipo
        colors = {'speed': (0, 255, 0), 'slow': (
            255, 255, 0), 'invulnerable': (255, 0, 0)}
        pygame.draw.rect(
            self.screen, colors[self.type], (self.position[0], self.position[1], self.size, self.size))

    def apply_effect(self, snake):
        if self.type == 'speed':
            snake.increase_speed(2)  # Aumenta la velocidad de la serpiente
        elif self.type == 'slow':
            snake.decrease_speed(1)  # Disminuye la velocidad de la serpiente
        elif self.type == 'invulnerable':
            # Hace a la serpiente invulnerable por 10 segundos
            snake.set_invulnerable(10)
        self.active = False
