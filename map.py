class Map:
    def __init__(self):
        self.tiles = []  # Aquí se pueden cargar mapas desde un archivo
    
    def draw(self, screen):
        for tile in self.tiles:
            screen.blit(tile.image, tile.rect)