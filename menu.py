import pygame
import sys

# Definir colores
WHITE = (255, 255, 255)
GRAY = (150, 150, 150)
BLUE = (0, 0, 255)

# Opciones del menú
MENU_OPTIONS = ["Jugar", "Opciones", "Mejores puntuaciones", "Salir"]

def draw_menu(screen, font, selected_option):
    """Dibuja el menú en la pantalla."""
    screen.fill(GRAY)  # Fondo gris

    for i, option in enumerate(MENU_OPTIONS):
        color = BLUE if i == selected_option else WHITE  # Resaltar opción seleccionada
        text = font.render(option, True, color)
        screen.blit(text, (300, 200 + i * 50))

    pygame.display.flip()

def menu(screen):
    """Función principal del menú."""
    pygame.init()
    font = pygame.font.Font(None, 36)
    selected_option = 0  # Índice de opción seleccionada

    while True:
        draw_menu(screen, font, selected_option)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected_option = (selected_option - 1) % len(MENU_OPTIONS)
                elif event.key == pygame.K_DOWN:
                    selected_option = (selected_option + 1) % len(MENU_OPTIONS)
                elif event.key == pygame.K_RETURN:
                    if selected_option == 0:  # Jugar
                        return "play"
                    elif selected_option == 1:  # Opciones
                        return "options"
                    elif selected_option == 2:  # Mejores puntuaciones
                        return "highscores"
                    elif selected_option == 3:  # Salir
                        pygame.quit()
                        sys.exit()
