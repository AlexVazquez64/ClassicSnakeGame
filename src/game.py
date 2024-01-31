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

# Bucle principal del juego
def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK) # Fondo de la ventana

        # Aquí irá la lógica del juego

        pygame.display.flip() # Actualizar la pantalla

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
