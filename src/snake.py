import pygame

# Colores
WHITE = (255, 255, 255)


class Snake:
    def __init__(self, screen, segment_size):
        self.screen = screen
        self.segment_size = segment_size
        self.segments = [pygame.Rect(100, 100, segment_size, segment_size)]
        # Moverse hacia la derecha inicialmente
        self.direction = pygame.Vector2(segment_size, 0)

    def draw(self):
        for segment in self.segments:
            pygame.draw.rect(self.screen, WHITE, segment)

    def move(self):
        head_x, head_y = self.segments[0].topleft
        new_head = pygame.Rect(head_x + self.direction.x, head_y +
                               self.direction.y, self.segment_size, self.segment_size)
        self.segments.insert(0, new_head)
        self.segments.pop()  # Eliminar el último segmento después de mover

    def grow(self):
        # Añadir un nuevo segmento sin eliminar el último, efectivamente creciendo
        head_x, head_y = self.segments[0].topleft
        new_head = pygame.Rect(head_x + self.direction.x, head_y +
                               self.direction.y, self.segment_size, self.segment_size)
        self.segments.insert(0, new_head)

    def change_direction(self, new_direction):
        # Evitar que la serpiente se mueva en la dirección opuesta directamente
        if self.direction.x + new_direction.x != 0 or self.direction.y + new_direction.y != 0:
            self.direction = new_direction

    def check_collision_with_self(self):
        # Comprobar colisión de la cabeza con el resto del cuerpo
        head = self.segments[0]
        return any(head.colliderect(segment) for segment in self.segments[1:])
