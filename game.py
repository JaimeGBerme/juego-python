from player import Player
from enemy import Enemy
#from collision import check_bullet_collisions
import collision
from bullet import disparo
from score import Score
import pygame
import random
import constantes   
import time
from level import Level  # Importar sistema de mapas

class Game:
    def __init__(self):      

        # Cargar nivel
        self.level = Level("Mapas\level1.txt")        

        #cargar jugador
        #self.player = Player(100, 300)        
        self.player = Player(self.level.player_start)        

        # Lista de enemigos
        self.enemies = []
        #self.enemies = [Enemy(constantes.WIDTH, random.randint(50,700))]  # Lista de enemigos        

        # Diccionario para controlar los tiempos de respawn
        self.enemy_spawn_timers = {point['pos']: time.time() for point in self.level.get_enemy_respawn_points()}

        self.score = Score()  # Instancia de la puntuación
        self.last_score_update = pygame.time.get_ticks()  # Control de tiempo para la puntuación        
        self.last_enemy_spawn = pygame.time.get_ticks()  # Control de tiempo respanw enemigos
    
    def update(self):
        # Comprobar colisiones con obstáculos
        '''
        if self.level.check_collision(self.player.rect):
            self.player.handle_collision()
        '''
        self.player.update(self.level)

        # Controlar el respawn de enemigos
        current_time = time.time()
        for point in self.level.get_enemy_respawn_points():
            pos = point['pos']
            frequency = point['frequency'] / 1000  # Convertir a segundos
            max_enemies = point['max_enemies']
            
            if current_time - self.enemy_spawn_timers[pos] >= frequency and len([e for e in self.enemies if e.spawn_point == pos]) < max_enemies:
                self.enemies.append(Enemy(pos))
                self.enemy_spawn_timers[pos] = current_time

        for enemy in self.enemies:
            enemy.update()
            '''
            if enemy.rect.x ==0 or (pygame.time.get_ticks() -self.last_enemy_spawn>2000):
                self.enemies.append(Enemy(1000, random.randint(50,700)))  #Añadimos un nuevo enemigo al salir el anterior de la pantalla
                self.last_enemy_spawn = pygame.time.get_ticks()
            '''
        # Verificar colisiones de balas
        collision.check_bullet_collisions(self.player, self.enemies, self.score)        

         # Verificar colisiones entre el jugador y los enemigos        
        if collision.check_collisions(self.player, self.enemies):
            self.score.reset()  # Reinicia la puntuación si colisiona
        
         # Aumentar puntuación cada 3 segundos si el jugador sobrevive
        if pygame.time.get_ticks() - self.last_score_update > 3000:
            self.score.increase(5)  # Suma 5 puntos cada 3 segundos
            self.last_score_update = pygame.time.get_ticks()
        

    def draw(self, screen):
        self.level.draw(screen)
        self.player.draw(screen)        
        for enemy in self.enemies:
            enemy.draw(screen)
        #for disparo in enemy.disparos:
        #    disparo.draw(screen)
        self.score.draw(screen)  # Dibuja la puntuación en pantalla

    