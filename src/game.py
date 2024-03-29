from obstacles import Obstacle
from food import Food
from snake import Snake
# Asegúrate de tener este archivo y función
from menu import show_start_screen, show_game_over_screen
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

# Direcciones como vectores
UP = pygame.Vector2(0, -20)
DOWN = pygame.Vector2(0, 20)
LEFT = pygame.Vector2(-20, 0)
RIGHT = pygame.Vector2(20, 0)


def handle_keyboard_events(event, snake):
    if event.key == pygame.K_UP:
        snake.change_direction(UP)
    elif event.key == pygame.K_DOWN:
        snake.change_direction(DOWN)
    elif event.key == pygame.K_LEFT:
        snake.change_direction(LEFT)
    elif event.key == pygame.K_RIGHT:
        snake.change_direction(RIGHT)


def game_loop(screen):
    global width, height
    score = 0
    font = pygame.font.SysFont(None, 55)
    last_score_increase = 0
    snake = Snake(screen, 20)
    food = Food(screen, width, height, 20)
    running = True
    clock = pygame.time.Clock()
    obstacles = [Obstacle(screen, width, height, 20)
                 for _ in range(5)]  # Ejemplo con 5 obstáculos

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                handle_keyboard_events(event, snake)

        snake.move()
        if snake.segments[0].topleft == food.position:
            score += 1
            food.respawn()
            snake.grow()
            if score % 5 == 0 and score != last_score_increase:  # Asegúrate de actualizar por nivel
                snake.update_level()
                # Actualiza la última puntuación en la que se incrementó el nivel
                last_score_increase = score

        if snake.check_collision_with_self() or not 0 <= snake.segments[0].x < width or not 0 <= snake.segments[0].y < height:
            show_game_over_screen(screen, font, score, snake.level)
            break

        head = snake.segments[0]
        for obstacle in obstacles:
            if head.colliderect(pygame.Rect(obstacle.position[0], obstacle.position[1], obstacle.size, obstacle.size)):
                # Manejar la colisión. Ejemplo: terminar el juego.
                show_game_over_screen(screen, font, score, snake.level)
                running = False
                break  # Sale del bucle y termina el juego

        screen.fill(BLACK)
        food.draw()
        snake.draw()
        # Dibuja cada obstáculo en la lista
        for obstacle in obstacles:
            obstacle.draw()
            
        score_text = font.render(
            f'Score: {score} - Level: {snake.level}', True, WHITE)
        screen.blit(score_text, (10, 10))
        pygame.display.flip()
        # Usa un tick fijo y maneja la velocidad en la serpiente
        clock.tick(snake.SNAKE_SPEED)


def main():
    font = pygame.font.SysFont(None, 55)
    while True:  # Añade un bucle aquí para permitir reiniciar el juego
        show_start_screen(screen, font)  # Mostrar pantalla de inicio
        game_loop(screen)  # Ejecuta el bucle principal del juego


if __name__ == '__main__':
    main()
