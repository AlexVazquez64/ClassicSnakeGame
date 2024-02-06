import pygame
import sys

# Colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Tamaño de la ventana (debería coincidir con la configuración en game.py)
width, height = 640, 480


def show_start_screen(screen, font):
    screen.fill(BLACK)  # Fondo negro
    title_text = font.render('Classic Snake Game', True, GREEN)
    start_text = font.render('Press any key to start', True, WHITE)

    # Centrar el texto
    title_rect = title_text.get_rect(center=(width / 2, height / 2 - 50))
    start_rect = start_text.get_rect(center=(width / 2, height / 2 + 10))

    screen.blit(title_text, title_rect)
    screen.blit(start_text, start_rect)
    pygame.display.flip()

    # Esperar a que el jugador presione una tecla para comenzar
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                return  # Comenzar el juego
            elif event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


def show_game_over_screen(screen, font, score, level):
    screen.fill(BLACK)  # Fondo negro
    game_over_text = font.render('Game Over!', True, RED)
    score_text = font.render(f'Score: {score}', True, WHITE)
    level_text = font.render(f'Level Reached: {level}', True, WHITE)
    restart_text = font.render(
        'Press Enter to Restart or ESC to Quit', True, WHITE)

    # Centrar el texto
    game_over_rect = game_over_text.get_rect(
        center=(width / 2, height / 2 - 60))
    score_rect = score_text.get_rect(center=(width / 2, height / 2 - 20))
    level_rect = level_text.get_rect(center=(width / 2, height / 2 + 20))
    restart_rect = restart_text.get_rect(center=(width / 2, height / 2 + 60))

    screen.blit(game_over_text, game_over_rect)
    screen.blit(score_text, score_rect)
    screen.blit(level_text, level_rect)
    screen.blit(restart_text, restart_rect)
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return  # Volver al juego
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            elif event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
