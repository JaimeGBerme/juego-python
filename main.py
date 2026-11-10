import modulo_funciones
import constantes
import pygame
import sys
from menu import menu
from game import Game

#from game import start_game
'''
modulo_funciones.imprimir_menu3(constantes.menu,0,2)
opción_menu: int=input("selecciona opción")
print (opción_menu)
if opción_menu == 1 :
    print ("1")
elif opción_menu == 2 :
    print ("2")
elif opción_menu == 3 :
    exit()
    print ("3")
   ''' 

    
# Inicialización
pygame.init()
#WIDTH, HEIGHT = 1024, 768
screen = pygame.display.set_mode((constantes.WIDTH, constantes.HEIGHT))
clock = pygame.time.Clock()


# Mostrar el menú antes de comenzar el juego
while True:
    option = menu(screen)

    if option == "play":
        # Cargar el juego
        game =Game()
        #game.start_game(screen)  # Función para iniciar el juego
        running = True
        while running:
            screen.fill((60, 60, 60))  # Fondo negro
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            game.update()
            game.draw(screen)

            pygame.display.flip()
            clock.tick(60)  # 60 FPS

        pygame.quit()
        sys.exit()
    elif option == "options":
        print("Opciones aún no implementadas.")
    elif option == "highscores":
        print("Mostrando mejores puntuaciones...")

'''
# Cargar el juego
game = Game()

running = True
while running:
    screen.fill((60, 60, 60))  # Fondo negro
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    game.update()
    game.draw(screen)

    pygame.display.flip()
    clock.tick(60)  # 60 FPS

pygame.quit()
'''


