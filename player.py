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
        self.gravity = 0.8
        self.jump_speed = -16

        self.on_floor = False
        self.on_ceiling = False
        self.on_left = False
        self.on_right = False

    def key_input(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_RIGHT]:
            self.direction.x = 1
        elif keys[pg.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0
        if keys[pg.K_SPACE] and self.on_floor:
            self.jump()
    
    def update_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        self.direction.y = self.jump_speed 

    def update(self):
        self.key_input()
