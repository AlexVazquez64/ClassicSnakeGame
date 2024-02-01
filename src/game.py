# Al principio de game.py, agrega la importación del nuevo módulo
from food import Food

import pygame
import sys

# Inicialización de Pygame
pygame.init()

# Configuraciones de la ventana
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Classic Snake Game')

# En la parte superior del archivo, define la puntuación inicial
score = 0

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

# Función para manejar los eventos del teclado


def handle_keyboard_events(event, direction):
    if event.key == pygame.K_UP and direction != DOWN:
        return UP
    elif event.key == pygame.K_DOWN and direction != UP:
        return DOWN
    elif event.key == pygame.K_LEFT and direction != RIGHT:
        return LEFT
    elif event.key == pygame.K_RIGHT and direction != LEFT:
        return RIGHT
    return direction

# Función para actualizar la posición de la serpiente


def update_snake_position(snake_segments, direction, food):
    global score  # Utiliza la variable global score

    head_x, head_y = snake_segments[0].topleft
    new_head = pygame.Rect(
        head_x + direction[0], head_y + direction[1], SEGMENT_SIZE, SEGMENT_SIZE)

    # Comprobar si la serpiente ha comido la comida
    if new_head.topleft == food.position:
        score += 1  # Aumentar la puntuación
        food.respawn()  # Hacer que la comida aparezca en una nueva posición
    else:
        # Si no ha comido, eliminar el último segmento
        snake_segments.pop()

    snake_segments.insert(0, new_head)

# Bucle principal del juego


def main():
    running = True
    direction = RIGHT  # Dirección inicial de la serpiente
    clock = pygame.time.Clock()  # Reloj para controlar la velocidad del juego
    # Al principio de main(), carga una fuente
    font = pygame.font.SysFont(None, 55)

    # Inicializar la serpiente
    snake_segments = [pygame.Rect(100, 100, SEGMENT_SIZE, SEGMENT_SIZE)]

    # Dentro de la función main(), después de inicializar la serpiente
    food = Food(screen, width, height, SEGMENT_SIZE)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                direction = handle_keyboard_events(event, direction)

        update_snake_position(snake_segments, direction, food)

        # Comprobar colisión con los bordes
        head_x, head_y = snake_segments[0].topleft
        if head_x < 0 or head_x >= width or head_y < 0 or head_y >= height:
            running = False  # Terminar el juego

        # Comprobar colisión consigo misma
        for segment in snake_segments[1:]:
            if snake_segments[0].colliderect(segment):
                running = False  # Terminar el juego

        screen.fill(BLACK)  # Fondo de la ventana
        # En el bucle principal, dibuja la comida llamando a food.draw()
        food.draw()
        draw_snake(screen, snake_segments)

        # Dentro del bucle principal, antes de pygame.display.flip()
        score_text = font.render(f'Score: {score}', True, WHITE)
        screen.blit(score_text, (10, 10))
        pygame.display.flip()  # Actualizar la pantalla
        clock.tick(SNAKE_SPEED)  # Controla la velocidad de actualización

    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()
