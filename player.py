import pygame as pg 
from settings import *

class Player(pg.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pg.Surface((tile_size/2, tile_size/2))
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect(topleft = pos)
