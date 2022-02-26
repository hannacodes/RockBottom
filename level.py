import pygame as pg

from tiles import *
from settings import *
from player import *

class Level: 
    def __init__(self, level_map, surf):
        self.display_surf = surf
        self.setup_map(level_map)
        self.shift_x = 0
        self.curr_x = 0
        
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
    
    '''
    Collision 
        1) apply vertical movement 
        2) check vertical collision 
        3) apply horizontal movement
        4) check horizontal collision 
    '''
    def vertical_collision(self):
        player = self.player.sprite
        player.update_gravity()
        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                    player.on_floor = True
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom 
                    player.direction.y = 0
                    player.on_ceiling = True

        if player.on_floor and player.direction.y < 0 or player.direction.y > 1: 
            player.on_floor = False
        if player.on_ceiling and player.direction.y > 0:
            player.on_ceiling = False


    def horizontal_collision(self):
        player = self.player.sprite 
        # apply horizontal movement
        player.rect.x += player.direction.x * player.speed 
        for sprite in self.tiles.sprites():
            # check horizontal collision
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                    self.curr_x = player.rect.left
                    player.on_left = True
                elif player.direction.x > 0: 
                    player.rect.right = sprite.rect.left
                    self.curr_x = player.rect.right
                    player.on_right = True
        
        if player.on_left and (player.rect.left < self.curr_x or player.direction.x >= 0):
            player.on_left = False
        if player.on_right and (player.rect.right > self.curr_x or player.direction.x <= 0):
            player.on_right = False

    def update(self):
        self.tiles.update(self.shift_x)
        self.tiles.draw(self.display_surf)
        self.scroll_x()

        player = self.player.sprite 
        if(player.rect.y > screen_height):
            return False

        self.player.update()
        self.vertical_collision()
        self.horizontal_collision()
        self.player.draw(self.display_surf)
        return True