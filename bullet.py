import pygame


class disparo:
    def __init__(self, x, y):
        self.image = pygame.Surface((20, 5))
        self.image.fill((150, 20,40))  # Rojo
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = 6

    def update(self):
        self.rect.x -= self.speed  # Movimiento simple hacia la izquierda
        
            
    def draw(self, screen):
        screen.blit(self.image, self.rect)

class Bullet:
    def __init__(self, x, y, direction, speed=5, color=(255, 255, 0)):
        """Crea una bala con posición, dirección y velocidad."""
        self.rect = pygame.Rect(x, y, 10, 5)  # Tamaño de la bala
        self.direction = direction  # -1 (izquierda) o 1 (derecha)
        self.speed = speed
        self.color = color

    def update(self):
        """Mueve la bala en su dirección."""
        self.rect.x += self.speed * self.direction

    def draw(self, screen):
        """Dibuja la bala en la pantalla."""
        pygame.draw.rect(screen, self.color, self.rect)