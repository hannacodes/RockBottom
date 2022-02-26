import pygame as pg

class Tile(pg.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        # creating surface with size by size
        self.image = pg.Surface((size, size))
        self.image.fill((120,120,120)) #gray tiles
        self.rect = self.image.get_rect(topleft = pos)
    #for scrolling
    def update(self, shift_x, shift_y):
        self.rect.x += shift_x
        self.rect.y += shift_y

class Spike(pg.sprite.Sprite):
    def __init__(self, pos, width, height):
        super().__init__()
        self.image = pg.Surface((width, height))
        self.image.fill((255,120,120))
        self.rect = self.image.get_rect(topleft = pos)
    def update(self, shift_x, shift_y):
        self.rect.x += shift_x
        self.rect.y += shift_y

class Boost(pg.sprite.Sprite):
    def __init__(self, pos, width, height):
        super().__init__()
        self.image = pg.Surface((width, height))
        self.image.fill((0, 200, 0))
        self.rect = self.image.get_rect(topleft = pos)
    def update(self, shift_x, shift_y):
        self.rect.x += shift_x
        self.rect.y += shift_y

class End(pg.sprite.Sprite):
    def __init__(self, pos, width, height):
        super().__init__()
        self.image = pg.Surface((width, height))
        self.image.fill((0, 0, 200))
        self.rect = self.image.get_rect(topleft = pos)
    def update(self, shift_x, shift_y):
        self.rect.x += shift_x
        self.rect.y += shift_y
