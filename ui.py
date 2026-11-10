import pygame

class UI:
    def __init__(self):
        self.font = pygame.font.Font(None, 30)
    
    def draw_health(self, screen, health):
        text = self.font.render(f"Vida: {health}", True, (255, 255, 255))
        screen.blit(text, (10, 10))
