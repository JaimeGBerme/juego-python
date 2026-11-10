import pygame
import re

class Level:
    def __init__(self, level_file):
        self.walls = []  # Lista de obstáculos
        self.enemy_respawn_points = []  # Lista de puntos de respawn
        self.load_level(level_file)


    def load_level(self, level_file):
        """Carga el nivel desde un archivo de texto usando un formato basado en paréntesis."""
        with open(level_file, 'r') as file:
            lines = file.readlines()

        for y, line in enumerate(lines):
            matches = re.finditer(r'\((.*?)\)', line.strip())  # Encuentra todos los elementos entre paréntesis
            x = 0
            for match in matches:
                content = match.group(1)  # Extrae el contenido dentro de los paréntesis
                if content == '#':
                    self.walls.append(pygame.Rect(x * 40, y * 40, 40, 40))  # Bloque colisionable
                elif content == 'P':
                    self.player_start = (x * 40, y * 40)  # Posición inicial del jugador
                elif content.startswith('R:'):
                    try:
                        parts = content[2:].split(',')
                        respawn_time = int(parts[0])  # Frecuencia de aparición (ms)
                        max_enemies = int(parts[1])  # Número máximo de enemigos en este punto
                        self.enemy_respawn_points.append({
                            'pos': (x * 40, y * 40),
                            'frequency': respawn_time,
                            'max_enemies': max_enemies
                        })
                    except:
                        print(f"Error en el formato del punto de respawn en ({x}, {y})")
                x += 1

    def draw(self, screen):
        """Dibuja los elementos del nivel en la pantalla."""
        for wall in self.walls:
            pygame.draw.rect(screen, (100, 100, 100), wall)  # Color gris para paredes
        for respawn in self.enemy_respawn_points:
            pygame.draw.circle(screen, (255, 0, 0), (respawn['pos'][0] + 20, respawn['pos'][1] + 20), 10)  # Rojo para puntos de respawn



    def check_collision(self, rect):
        """Comprueba si el jugador colisiona con algún obstáculo."""
        return any(rect.colliderect(wall) for wall in self.walls)
    
    def get_enemy_respawn_points(self):
        """Devuelve los puntos de respawn de enemigos."""
        return self.enemy_respawn_points