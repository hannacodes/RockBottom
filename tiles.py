import pygame as pg
from player import *
from level import *

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
            elif col == 'O':
                self.image = pg.image.load("art_assets/forest-level/tile/pipe-tile-continued.png").convert_alpha()
            elif col == 'L':
                self.image = pg.image.load("art_assets/forest-level/tile/forest-tiles-left-sharp.png").convert_alpha()
                self.image = pg.transform.rotozoom(self.image, 0, (size/28))
            elif col == 'K':
                self.image = pg.image.load("art_assets/forest-level/tile/forest-tiles-right-sharp.png").convert_alpha()
                self.image = pg.transform.rotozoom(self.image, 0, (size/28))
            elif col == 'N':
                self.image = pg.image.load("art_assets/forest-level/platform/forest-platforms-left.png").convert_alpha()
                self.image = pg.transform.rotozoom(self.image, 0, (size/28))
            elif col == 'M':
                self.image = pg.image.load("art_assets/forest-level/platform/forest-platforms-right.png").convert_alpha()
                self.image = pg.transform.rotozoom(self.image, 0, (size/28))
            elif col == 'V':
                self.image = pg.image.load("art_assets/forest-level/platform/forest-single-platform.png").convert_alpha()
                self.image = pg.transform.rotozoom(self.image, 0, (size/28))
        if lvl == 2:
            if col == 'X':
                self.image = pg.image.load("art_assets/city-level/platforms-and-tiles/city-tile-middle.png").convert_alpha()
            if col == 'F':
                self.image = pg.image.load("art_assets/city-level/platforms-and-tiles/city-platform-single.png").convert_alpha()
                self.image = pg.transform.rotozoom(self.image, 0, (size/28))
            if col == 'O':
                self.image = pg.image.load("art_assets/city-level/platforms-and-tiles/city-tiles-around-shans-door.png").convert_alpha()
            if col == 'T':
                self.image = pg.image.load("art_assets/city-level/platforms-and-tiles/city-tile-middle-window.png").convert_alpha()
            elif col == 'L':
                self.image = pg.image.load("art_assets/city-level/platforms-and-tiles/city-tile-left.png").convert_alpha()
            elif col == 'K':
                self.image = pg.image.load("art_assets/city-level/platforms-and-tiles/city-tile-right.png").convert_alpha()
            elif col == 'M':
                self.image = pg.image.load("art_assets/forest-level/tile/pipe-tile-continued.png").convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
    #for scrolling
    def update(self, shift_x, shift_y):
        self.rect.x += shift_x
        self.rect.y += shift_y

class Spike(pg.sprite.Sprite):
    def __init__(self, pos, col, lvl):
        super().__init__()
        if lvl == 1:
            self.image = pg.image.load("art_assets/forest-level/poison/poison-middle-new.png").convert_alpha()
        if lvl == 2:
            if col == 'R':
                self.image = pg.image.load("art_assets/city-level/rat.png").convert_alpha()
            if col == 'S':
                self.image = pg.image.load("art_assets/city-level/drone.png").convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
    def update(self, shift_x, shift_y):
        self.rect.x += shift_x
        self.rect.y += shift_y

class Boost(pg.sprite.Sprite):
    def __init__(self, pos, lvl):
        super().__init__()
        if lvl == 1:
            self.image = pg.image.load("art_assets/forest-level/bouncy-mushroom.png").convert_alpha()
        if lvl == 2:
            self.image = pg.image.load("art_assets/city-level/bouncy-city-awning-darker.png").convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
    def update(self, shift_x, shift_y):
        self.rect.x += shift_x
        self.rect.y += shift_y

class End(pg.sprite.Sprite):
    def __init__(self, pos, lvl):
        super().__init__()
        if lvl == 1:
            self.image = pg.image.load("art_assets/forest-level/tile/pipe-entrance.png").convert_alpha()
        elif lvl == 2:
            self.image = pg.image.load("art_assets/city-level/platforms-and-tiles/city-tile-shans-door.png").convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
    def update(self, shift_x, shift_y):
        self.rect.x += shift_x
        self.rect.y += shift_y
