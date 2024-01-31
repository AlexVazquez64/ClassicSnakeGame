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

# Tamaño del segmento de la serpiente
SEGMENT_SIZE = 20

# Función para dibujar la serpiente
def draw_snake(screen, snake_segments):
    for segment in snake_segments:
        pygame.draw.rect(screen, WHITE, segment)

# Bucle principal del juego
def main():
    running = True

    # Inicializar la serpiente
    snake_segments = [pygame.Rect(100, 100, SEGMENT_SIZE, SEGMENT_SIZE)]

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK) # Fondo de la ventana
        # Lógica del juego
        draw_snake(screen, snake_segments)

        # Aquí irá la lógica del juego

        pygame.display.flip() # Actualizar la pantalla

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
