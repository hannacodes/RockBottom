import pygame as pg

from tiles import *
from settings import *
from player import *

class Level: 
    def __init__(self, level_map, surf, lvl):
        self.display_surf = surf
        self.lvl = lvl
        self.setup_map(level_map)
        self.shift_x = 0
        self.curr_x = 0

        self.shift_y = 0
        
    def setup_map(self, level_map):
        self.tiles = pg.sprite.Group()
        self.player = pg.sprite.GroupSingle()
        self.spikes = pg.sprite.Group()
        self.boosts = pg.sprite.Group()
        self.end = pg.sprite.GroupSingle()

        for row_index, row in enumerate(level_map):
            for col_index, col in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size
                if col == 'X' or col == 'T' or col == 'F':
                    tile = Tile((x, y), col, tile_size, self.lvl)
                    self.tiles.add(tile)
                if col == 'P':
                    y += tile_size/2
                    rock = Player((x,y))
                    self.player.add(rock)
                if col == 'S':
                    y += tile_size/2
                    spike = Spike((x,y), self.lvl)
                    self.spikes.add(spike)
                if col == 'B':
                    y += tile_size/2
                    boost = Boost((x,y), self.lvl)
                    self.boosts.add(boost)
                if col == 'E':
                    end = End((x,y), tile_size/2, tile_size)
                    self.end.add(end)

    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x
        speed = 6

        if player_x < screen_width/4 and direction_x < 0:
            self.shift_x = speed 
            player.speed.x = 0
        elif player_x > screen_width-(screen_width/4) and direction_x > 0:
            self.shift_x = -speed
            player.speed.x = 0
        else:
            self.shift_x = 0
            player.speed.x = speed
    
    def scroll_y(self):
        player = self.player.sprite
        player_y = player.rect.centery
        direction_y = player.direction.y
        speed = 6
        
        if player_y < screen_height/4 and direction_y < 0:
            self.shift_y = speed 
            player.speed.y = 0
        elif player_y > screen_height-(screen_height/4) and direction_y > 0:
            self.shift_y = -speed
            player.speed.y = 0
        else:
            self.shift_y = 0
            player.speed.y = speed

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
        player.rect.x += player.direction.x * player.speed.x
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

    def spike_collide(self):
        player = self.player.sprite
        if pg.sprite.spritecollideany(player, self.spikes):
            return True
        return False
    
    def boost_collide(self):
        player = self.player.sprite 
        if pg.sprite.spritecollideany(player, self.boosts):
            player.jump_speed = -20
            player.jump()
        else:
            player.jump_speed = -16

    def end_collide(self):
        player = self.player.sprite
        if pg.sprite.spritecollideany(player, self.end):
            return True
        return False

    def update_tile(self, sprites):
        sprites.update( self.shift_x, self.shift_y)
        sprites.draw(self.display_surf)

    def isEnd(self):
        return self.end_collide()

    def update(self):
        self.update_tile(self.tiles)
        self.update_tile(self.spikes)
        self.update_tile(self.boosts)
        self.update_tile(self.end)
        self.boost_collide()
        self.scroll_x()
        self.scroll_y()
        player = self.player.sprite 
        if(player.rect.y > screen_height) or self.spike_collide():
            return False

        self.player.update()
        self.vertical_collision()
        self.horizontal_collision()
        self.player.draw(self.display_surf)
        return True