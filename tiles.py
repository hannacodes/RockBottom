import pygame as pg

class Tile(pg.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        # creating surface with size by size
        self.image = pg.Surface((size, size))
        self.image.fill((120,120,120)) #gray tiles
        self.rect = self.image.get_rect(topleft = pos)
