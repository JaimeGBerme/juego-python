import pygame
import time
import constantes
from bullet import Bullet
class Player:
    def __init__(self, start_pos):
        self.image = pygame.Surface((40, 40))
        self.image.fill((0, 255, 0))  # Verde por defecto        
        self.rect = self.image.get_rect(topleft=start_pos)        

        # Físicas del movimiento
        self.vel_x = 0
        self.vel_y = 0
        self.acceleration = 0.8   # Aceleración al moverse
        self.friction = 0.8       # Inercia (resistencia)
        self.max_speed = 6        # Velocidad máxima
        self.frozen = False       # Estado de congelamiento
        self.freeze_time = 0
        self.bullets = []  # Lista de balas del jugador
        self.last_shot_time = pygame.time.get_ticks()  # Tiempo del último disparo

    def freeze(self):
        """Congela al jugador por 1 segundo y cambia su color."""
        self.frozen = True
        self.freeze_time = time.time() + 0.7  # Tiempo actual + 0.5 segundo
        self.image.fill((255, 255, 0))  # Cambia a amarillo
        self.vel_x = 0
        self.vel_y = 0  # Detiene al jugador completamente

    def update(self,level):
        """Maneja el movimiento del jugador con aceleración e inercia."""
        if self.frozen:
            if time.time() > self.freeze_time:  # Si pasó 1 segundo
                self.frozen = False
                self.image.fill((0, 255, 0))  # Vuelve a verde
            return  # No permite mover mientras está congelado

        keys = pygame.key.get_pressed()

        # Aceleración en X
        if keys[pygame.K_LEFT]:
            self.vel_x -= self.acceleration
        elif keys[pygame.K_RIGHT]:
            self.vel_x += self.acceleration
        
        # Aceleración en Y
        if keys[pygame.K_UP]:
            self.vel_y -= self.acceleration
        elif keys[pygame.K_DOWN]:
            self.vel_y += self.acceleration
        
        # Aplicar fricción (inercia) cuando no hay entrada de movimiento
        if not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
            self.vel_x *= self.friction
        if not keys[pygame.K_UP] and not keys[pygame.K_DOWN]:
            self.vel_y *= self.friction

        # **Disparar con la tecla espacio y ha pasado 0,5 segundo**
        if keys[pygame.K_SPACE] and (pygame.time.get_ticks() - self.last_shot_time > 500):
            self.shoot()
            self.last_shot_time = pygame.time.get_ticks()
                        
         # Actualizar las balas
        for bullet in self.bullets:
            bullet.update()

        # Eliminar balas fuera de la pantalla
        self.bullets = [b for b in self.bullets if b.rect.x < constantes.WIDTH]  # Suponiendo ancho de pantalla

        # Limitar la velocidad máxima
        self.vel_x = max(-self.max_speed, min(self.max_speed, self.vel_x))
        self.vel_y = max(-self.max_speed, min(self.max_speed, self.vel_y))
        
        # Calcular nueva posición
        new_x = self.rect.x + int(self.vel_x)
        new_y = self.rect.y + int(self.vel_y)
        '''
        # **Actualizar la posición con límites de pantalla**
        self.rect.x += int(self.vel_x)
        self.rect.y += int(self.vel_y)
        # **Corrección: Asegurar que no salga de los bordes**
        if self.rect.left < 0:
            self.rect.left = 0
            self.vel_x = 0  # Detener el movimiento al chocar con el borde izquierdo
        elif self.rect.right > constantes.WIDTH:
            self.rect.right = constantes.WIDTH
            self.vel_x = 0  # Detener el movimiento al chocar con el borde derecho

        if self.rect.top < 0:
            self.rect.top = 0
            self.vel_y = 0  # Detener el movimiento al chocar con el borde superior
        elif self.rect.bottom > constantes.HEIGHT:
            self.rect.bottom = constantes.HEIGHT
            self.vel_y = 0  # Detener el movimiento al chocar con el borde inferior
        '''

    # Comprobar colisiones con obstáculos
        if not level.check_collision(pygame.Rect(new_x, self.rect.y, self.rect.width, self.rect.height)):
            if 0 <= new_x <= constantes.WIDTH - self.rect.width:
                self.rect.x = new_x
        else:
            self.vel_x = 0  # Detener movimiento horizontal en colisión

        if not level.check_collision(pygame.Rect(self.rect.x, new_y, self.rect.width, self.rect.height)):
            if 0 <= new_y <= constantes.HEIGHT - self.rect.height:
                self.rect.y = new_y
        else:
            self.vel_y = 0  # Detener movimiento vertical en colisión        

    def shoot(self):
        """Crea una nueva bala y la añade a la lista."""
        new_bullet = Bullet(self.rect.right, self.rect.centery, direction=1,speed=10)
        self.bullets.append(new_bullet)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
         #pygame.draw.rect(screen, (0, 0, 255), self.rect)  # Dibuja al jugador
        for bullet in self.bullets:
            bullet.draw(screen)
    def handle_collision(self):
        """Evita que el jugador atraviese obstáculos."""
        self.freeze()
        #self.vel_x = 0
        #self.vel_y = 0

    
