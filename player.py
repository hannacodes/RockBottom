import pygame as pg 
from settings import *

class Player(pg.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pg.Surface((tile_size/2, tile_size/2))
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect(topleft = pos)

        # direction has both x and y
        self.direction = pg.math.Vector2()
        self.speed = 6

    def key_input(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_RIGHT]:
            self.direction.x = 1
        elif keys[pg.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0
    
    def update(self):
        self.key_input()
        self.rect.x += self.direction.x * self.speed
