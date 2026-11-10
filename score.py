import pygame

class Score:
    def __init__(self):
        self.points = 0
        self.font = pygame.font.Font(None, 30)  # Fuente predeterminada

    def increase(self, amount=10):
        """Aumenta la puntuación."""
        self.points += amount

    def reset(self):
        """Reinicia la puntuación."""
        self.points = 0

    def draw(self, screen):
        """Dibuja la puntuación en pantalla."""
        score_text = self.font.render(f"Puntuación: {self.points}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))  # Esquina superior izquierda
