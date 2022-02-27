import pygame as pg 
from settings import *

class Player(pg.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.sprites = []
        size = (32, 32)
        self.sprites.append(pg.transform.scale(pg.image.load('art_assets/pet-rock/rolling/rock-pet-animation-frames(1).png'), size))
        self.sprites.append(pg.transform.scale(pg.image.load('art_assets/pet-rock/rolling/rock-pet-animation-frames(2).png'), size))
        self.sprites.append(pg.transform.scale(pg.image.load('art_assets/pet-rock/rolling/rock-pet-animation-frames(3).png'), size))
        self.sprites.append(pg.transform.scale(pg.image.load('art_assets/pet-rock/rolling/rock-pet-animation-frames(4).png'), size))
        self.sprites.append(pg.transform.scale(pg.image.load('art_assets/pet-rock/rolling/rock-pet-animation-frames(5).png'), size))
        self.sprites.append(pg.transform.scale(pg.image.load('art_assets/pet-rock/rolling/rock-pet-animation-frames(6).png'), size))
        self.sprites.append(pg.transform.scale(pg.image.load('art_assets/pet-rock/rolling/rock-pet-animation-frames(7).png'), size))
        self.sprites.append(pg.transform.scale(pg.image.load('art_assets/pet-rock/rolling/rock-pet-animation-frames(8).png'), size))
        self.sprites.append(pg.transform.scale(pg.image.load('art_assets/pet-rock/rolling/rock-pet-animation-frames(9).png'), size))
        self.sprites.append(pg.transform.scale(pg.image.load('art_assets/pet-rock/rolling/rock-pet-animation-frames(10).png'), size))
        self.sprites.append(pg.transform.scale(pg.image.load('art_assets/pet-rock/rolling/rock-pet-animation-frames(11).png'), size))
        self.sprites.append(pg.transform.scale(pg.image.load('art_assets/pet-rock/rolling/rock-pet-animation-frames(12).png'), size))
        self.sprites.append(pg.transform.scale(pg.image.load('art_assets/pet-rock/rolling/rock-pet-animation-frames(13).png'), size))
        self.sprites.append(pg.transform.scale(pg.image.load('art_assets/pet-rock/rolling/rock-pet-animation-frames(14).png'), size))
        self.sprites.append(pg.transform.scale(pg.image.load('art_assets/pet-rock/rolling/rock-pet-animation-frames(15).png'), size))
        self.sprites.append(pg.transform.scale(pg.image.load('art_assets/pet-rock/rolling/rock-pet-animation-frames(16).png'), size))
        self.sprites.append(pg.transform.scale(pg.image.load('art_assets/pet-rock/rolling/rock-pet-animation-frames(17).png'), size))
        self.sprites.append(pg.transform.scale(pg.image.load('art_assets/pet-rock/rolling/rock-pet-animation-frames(18).png'), size))
        self.sprites.append(pg.transform.scale(pg.image.load('art_assets/pet-rock/rolling/rock-pet-animation-frames(19).png'), size))
        self.sprites.append(pg.transform.scale(pg.image.load('art_assets/pet-rock/rolling/rock-pet-animation-frames(20).png'), size))
        self.sprites.append(pg.transform.scale(pg.image.load('art_assets/pet-rock/rolling/rock-pet-animation-frames(21).png'), size))
        self.sprites.append(pg.transform.scale(pg.image.load('art_assets/pet-rock/rolling/rock-pet-animation-frames(22).png'), size))
        self.sprites.append(pg.transform.scale(pg.image.load('art_assets/pet-rock/rolling/rock-pet-animation-frames(23).png'), size))
        self.sprites.append(pg.transform.scale(pg.image.load('art_assets/pet-rock/rolling/rock-pet-animation-frames(24).png'), size))

        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.image = pg.image.load("art_assets/pet-rock/rock-pet-animation-stand.png").convert_alpha()
        self.image = pg.transform.rotozoom(self.image, 0, ((tile_size/2)/14))
        self.rect = self.image.get_rect(topleft = pos)

        # direction has both x and y
        self.direction = pg.math.Vector2()
        self.speed = pg.math.Vector2()
        self.speed.x = 6
        self.speed.y = 6
        self.gravity = 0.8
        self.jump_speed = -14

        self.on_floor = False
        self.on_ceiling = False
        self.on_left = False
        self.on_right = False
        self.is_animating = False

        #status of player for animation

        self.on_right = False
        self.on_left = False
        self.on_ceiling = False
        self.on_floor = False
        self.facing_right = True

        
    def get_status(self):
        if self.direction.y < 0:
            self.status = self.animate()
        elif self.direction.y > 1:
            self.status = self.animate()
        else:
            if self.direction.x != 0:
                self.status = self.animate()
            else:
                self.status = 'art_assets/pet-rock/rock-pet-animation-stand-32-32.png'
        


    def animate(self):
        self.is_animating = True

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
        if self.direction.x and self.direction.y != 0:
           self.is_animating == True
           self.current_sprite += 0.8

           if self.current_sprite >= len(self.sprites):
              self.current_sprite = 0
              self.is_animating = False
        else:
            self.is_animating = False
            self.status = 'art_assets/pet-rock/rock-pet-animation-stand-32-32.png'

            self.image = self.sprites[int(self.current_sprite)]
        self.animate()
