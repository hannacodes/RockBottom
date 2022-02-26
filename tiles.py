import pygame as pg

class Tile(pg.sprite.Sprite):
    def __init__(self, pos, col, size, lvl):
        super().__init__()
        if lvl == 1:
            if col == 'T':
                self.image = pg.image.load("art_assets/forest-level/tile/forest-tile-middle.png").convert_alpha()
                self.image = pg.transform.rotozoom(self.image, 0, (size/28))
            elif col == 'X':
                self.image = pg.image.load("art_assets/forest-level/tile/forest-tiles-dirt.png").convert_alpha()
                self.image = pg.transform.rotozoom(self.image, 0, (size/28))
            elif col == 'F':
                self.image = pg.image.load("art_assets/forest-level/platform/forest-platforms-middle.png").convert_alpha()
                self.image = pg.transform.rotozoom(self.image, 0, (size/28))
        self.rect = self.image.get_rect(topleft = pos)
    #for scrolling
    def update(self, shift_x, shift_y):
        self.rect.x += shift_x
        self.rect.y += shift_y

class Spike(pg.sprite.Sprite):
    def __init__(self, pos, lvl):
        super().__init__()
        if lvl == 1:
            self.image = pg.image.load("art_assets/forest-level/poison/poison-middle-new.png").convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
    def update(self, shift_x, shift_y):
        self.rect.x += shift_x
        self.rect.y += shift_y

class Boost(pg.sprite.Sprite):
    def __init__(self, pos, lvl):
        super().__init__()
        if lvl == 1:
            self.image = pg.image.load("art_assets/forest-level/bouncy-mushroom.png").convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
    def update(self, shift_x, shift_y):
        self.rect.x += shift_x
        self.rect.y += shift_y

class End(pg.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pg.image.load("art_assets/end-flag.png").convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
    def update(self, shift_x, shift_y):
        self.rect.x += shift_x
        self.rect.y += shift_y
