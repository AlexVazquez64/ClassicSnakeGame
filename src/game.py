from food import Food
from snake import Snake
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

# Direcciones como vectores
UP = pygame.Vector2(0, -SEGMENT_SIZE)
DOWN = pygame.Vector2(0, SEGMENT_SIZE)
LEFT = pygame.Vector2(-SEGMENT_SIZE, 0)
RIGHT = pygame.Vector2(SEGMENT_SIZE, 0)


def handle_keyboard_events(event, snake):
    if event.key == pygame.K_UP:
        snake.change_direction(UP)
    elif event.key == pygame.K_DOWN:
        snake.change_direction(DOWN)
    elif event.key == pygame.K_LEFT:
        snake.change_direction(LEFT)
    elif event.key == pygame.K_RIGHT:
        snake.change_direction(RIGHT)
        
# Bucle principal del juego


def main():
    global score  # Añade esta línea
    running = True
    clock = pygame.time.Clock()  # Reloj para controlar la velocidad del juego
    font = pygame.font.SysFont(None, 55)  # Fuente para el puntaje

    snake = Snake(screen, SEGMENT_SIZE)  # Inicializar la serpiente
    food = Food(screen, width, height, SEGMENT_SIZE)  # Inicializar la comida

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                direction = handle_keyboard_events(event, snake)

        snake.move()
        if snake.segments[0].topleft == food.position:
            score += 1
            food.respawn()
            snake.grow()

        if snake.check_collision_with_self() or not 0 <= snake.segments[0].x < width or not 0 <= snake.segments[0].y < height:
            running = False  # Terminar el juego si hay colisión

        screen.fill(BLACK)
        food.draw()
        snake.draw()

        score_text = font.render(f'Score: {score}', True, WHITE)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()
        clock.tick(SNAKE_SPEED)

    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()
