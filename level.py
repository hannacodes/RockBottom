import pygame as pg

from tiles import *
from settings import *

class Level: 
    def __init__(self, level_map, surf):
        self.display_surf = surf
        self.setup_map(level_map)
        
    def setup_map(self, level_map):
        self.tiles = pg.sprite.Group()

        for row_index, row in enumerate(level_map):
            for col_index, col in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size
                if col == 'X':
                    tile = Tile((x, y), tile_size)
                    self.tiles.add(tile)

    def run(self):
        self.tiles.draw(self.display_surf)