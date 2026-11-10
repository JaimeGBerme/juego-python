import pygame
import time

def check_collisions(player, enemies):
    for enemy in enemies:
        if player.rect.colliderect(enemy.rect):  # Detecta colisión
            player.freeze()
            enemies.remove(enemy)  # Eliminar enemigo
            return True  # Indica que hubo colisión    
    return False  # No hubo colisión

def check_bullet_collisions(player, enemies, score):
    """Verifica colisiones entre balas y enemigos o jugador."""
    # Revisar si las balas del jugador golpean enemigos
    for bullet in player.bullets[:]:
        for enemy in enemies[:]:
            if bullet.rect.colliderect(enemy.rect):
                player.bullets.remove(bullet)  # Eliminar la bala
                enemies.remove(enemy)  # Eliminar enemigo
                score.increase(20)  # Aumentar puntuación

    # Revisar si balas de enemigos golpean al jugador
    for enemy in enemies:
        for bullet in enemy.bullets[:]:
            if bullet.rect.colliderect(player.rect):
                enemy.bullets.remove(bullet)  # Eliminar la bala
                score.reset()  # Reiniciar puntuación
                player.freeze()
            if player.rect.colliderect(enemy.rect):  # Detecta colisión entre jugador y nave enemiga
                score.reset()  # Reiniciar puntuación
                player.freeze()
    