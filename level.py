import pygame as pg

from tiles import *
from settings import *
from player import *

class Level: 
    def __init__(self, level_map, surf):
        self.display_surf = surf
        self.setup_map(level_map)
        self.shift_x = 0
        
    def setup_map(self, level_map):
        self.tiles = pg.sprite.Group()
        self.player = pg.sprite.GroupSingle()

        for row_index, row in enumerate(level_map):
            for col_index, col in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size
                if col == 'X':
                    tile = Tile((x, y), tile_size)
                    self.tiles.add(tile)
                if col == 'P':
                    y += tile_size/2
                    rock = Player((x,y))
                    self.player.add(rock)

    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x
        speed = 6

        if player_x < screen_width/4 and direction_x < 0:
            self.shift_x = speed 
            player.speed = 0
        elif player_x > screen_width-(screen_width/4) and direction_x > 0:
            self.shift_x = -speed
            player.speed = 0
        else:
            self.shift_x = 0
            player.speed = speed


    def update(self):
        self.tiles.update(self.shift_x)
        self.tiles.draw(self.display_surf)
        self.scroll_x()

        self.player.update()
        self.player.draw(self.display_surf)