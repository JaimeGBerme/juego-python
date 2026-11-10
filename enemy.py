import pygame
import constantes
from bullet import Bullet

class Enemy:
    def __init__(self, start_pos):
        self.image = pygame.Surface((40, 40))
        self.image.fill((255, 0, 0))  # Rojo
        self.rect = self.image.get_rect(topleft=start_pos)
        #self.vel_x = random.choice([-2, 2])
        #self.vel_y = random.choice([-2, 2])
        self.speed = 4        
        self.bullets = []
        self.last_shot_time = pygame.time.get_ticks()  # Tiempo del último disparo
        self.spawn_point = start_pos  # Guarda el punto de aparición
    def update(self):
        self.rect.x -= self.speed  # Movimiento simple hacia la izquierda
        '''
        if self.rect.x % 60 ==0 and len(self.disparos)<4:
        #if  len(self.disparos)<4:
            self.disparar (self.rect.x+self.pos_disparo_x ,self.rect.y+self.pos_disparo_y)
        '''
        # Disparar cada 2 segundos
        if pygame.time.get_ticks() - self.last_shot_time > 2000:
            self.shoot()
            self.last_shot_time = pygame.time.get_ticks()

        # Actualizar balas
        for bullet in self.bullets:
            bullet.update()

        # Eliminar balas fuera de la pantalla
        self.bullets = [b for b in self.bullets if b.rect.x > 0 and b.rect.x < constantes.WIDTH]
            
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        #pygame.draw.rect(screen, (255, 0, 0), self.rect)  # Dibuja al enemigo
        for bullet in self.bullets:
            bullet.draw(screen)
    def shoot(self):
        """Crea una bala y la añade a la lista."""
        new_bullet = Bullet(self.rect.left, self.rect.centery, direction=-1,speed=10, color=(255, 0, 0))
        self.bullets.append(new_bullet)

    #def disparar (self,x,y):
        #self.disparos.append(proyectiles.disparo(x, y))  # Lista de disparos
    
