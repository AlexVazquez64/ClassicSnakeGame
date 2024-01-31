import pygame
import sys

# Inicialización de Pygame
pygame.init()

# Configuraciones de la ventana
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Classic Snake Game')

# Colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Tamaño del segmento de la serpiente y velocidad
SEGMENT_SIZE = 20
SNAKE_SPEED = 5

# Direcciones
UP = (0, -SEGMENT_SIZE)
DOWN = (0, SEGMENT_SIZE)
LEFT = (-SEGMENT_SIZE, 0)
RIGHT = (SEGMENT_SIZE, 0)

# Función para dibujar la serpiente


def draw_snake(screen, snake_segments):
    for segment in snake_segments:
        pygame.draw.rect(screen, WHITE, segment)

# Bucle principal del juego


def main():
    running = True
    direction = RIGHT  # Dirección inicial de la serpiente
    clock = pygame.time.Clock()  # Reloj para controlar la velocidad del juego

    # Inicializar la serpiente
    snake_segments = [pygame.Rect(100, 100, SEGMENT_SIZE, SEGMENT_SIZE)]

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != DOWN:
                    direction = UP
                elif event.key == pygame.K_DOWN and direction != UP:
                    direction = DOWN
                elif event.key == pygame.K_LEFT and direction != RIGHT:
                    direction = LEFT
                elif event.key == pygame.K_RIGHT and direction != LEFT:
                    direction = RIGHT

        # Mover la serpiente
        head_x, head_y = snake_segments[0].topleft
        new_head = pygame.Rect(
            head_x + direction[0], head_y + direction[1], SEGMENT_SIZE, SEGMENT_SIZE)
        snake_segments.insert(0, new_head)
        if len(snake_segments) > 1:  # Evita eliminar el segmento si solo hay uno
            snake_segments.pop()

        screen.fill(BLACK)  # Fondo de la ventana
        draw_snake(screen, snake_segments)

        pygame.display.flip()  # Actualizar la pantalla
        clock.tick(SNAKE_SPEED)  # Controla la velocidad de actualización

    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()
