import pygame

# Define nuevos colores para la serpiente
HEAD_COLOR = (70, 130, 180)  # Un color más oscuro para la cabeza
BODY_COLOR = (34, 139, 34)  # Un color verde para el cuerpo


class Snake:
    def __init__(self, screen, segment_size):
        self.screen = screen
        self.segment_size = segment_size
        self.segments = [pygame.Rect(100, 100, segment_size, segment_size)]
        # Moverse hacia la derecha inicialmente
        self.direction = pygame.Vector2(segment_size, 0)

    def draw(self):
        for i, segment in enumerate(self.segments):
            # Dibuja un círculo para cada segmento
            pos = segment.center  # Obtiene la posición central del segmento para el círculo
            if i == 0:  # Si es la cabeza, usa el color de la cabeza
                pygame.draw.circle(self.screen, HEAD_COLOR,
                                   pos, self.segment_size // 2)
            else:  # Para el resto del cuerpo, usa el color del cuerpo
                pygame.draw.circle(self.screen, BODY_COLOR,
                                   pos, self.segment_size // 2)

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
