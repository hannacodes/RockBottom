import pygame as pg

from tiles import *
from settings import *
from player import *

class Level: 
    def __init__(self, level_map, surf):
        self.display_surf = surf
        self.setup_map(level_map)
        
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



    def run(self):
        self.tiles.draw(self.display_surf)

        self.player.draw(self.display_surf)