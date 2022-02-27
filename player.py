import pygame as pg 
from settings import *

class Player(pg.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.sprites = []
        self.sprites.append(pg.image.load('art_assets/pet-rock/rolling/rock-pet-animation-frames(1).png'))
        self.sprites.append(pg.image.load('art_assets/pet-rock/rolling/rock-pet-animation-frames(2).png'))
        self.sprites.append(pg.image.load('art_assets/pet-rock/rolling/rock-pet-animation-frames(3).png'))
        self.sprites.append(pg.image.load('art_assets/pet-rock/rolling/rock-pet-animation-frames(4).png'))
        self.sprites.append(pg.image.load('art_assets/pet-rock/rolling/rock-pet-animation-frames(5).png'))
        self.sprites.append(pg.image.load('art_assets/pet-rock/rolling/rock-pet-animation-frames(6).png'))
        self.sprites.append(pg.image.load('art_assets/pet-rock/rolling/rock-pet-animation-frames(7).png'))
        self.sprites.append(pg.image.load('art_assets/pet-rock/rolling/rock-pet-animation-frames(8).png'))
        self.sprites.append(pg.image.load('art_assets/pet-rock/rolling/rock-pet-animation-frames(9).png'))
        self.sprites.append(pg.image.load('art_assets/pet-rock/rolling/rock-pet-animation-frames(10).png'))
        self.sprites.append(pg.image.load('art_assets/pet-rock/rolling/rock-pet-animation-frames(11).png'))
        self.sprites.append(pg.image.load('art_assets/pet-rock/rolling/rock-pet-animation-frames(12).png'))
        self.sprites.append(pg.image.load('art_assets/pet-rock/rolling/rock-pet-animation-frames(13).png'))
        self.sprites.append(pg.image.load('art_assets/pet-rock/rolling/rock-pet-animation-frames(14).png'))
        self.sprites.append(pg.image.load('art_assets/pet-rock/rolling/rock-pet-animation-frames(15).png'))
        self.sprites.append(pg.image.load('art_assets/pet-rock/rolling/rock-pet-animation-frames(16).png'))
        self.sprites.append(pg.image.load('art_assets/pet-rock/rolling/rock-pet-animation-frames(17).png'))
        self.sprites.append(pg.image.load('art_assets/pet-rock/rolling/rock-pet-animation-frames(18).png'))
        self.sprites.append(pg.image.load('art_assets/pet-rock/rolling/rock-pet-animation-frames(19).png'))
        self.sprites.append(pg.image.load('art_assets/pet-rock/rolling/rock-pet-animation-frames(20).png'))
        self.sprites.append(pg.image.load('art_assets/pet-rock/rolling/rock-pet-animation-frames(21).png'))
        self.sprites.append(pg.image.load('art_assets/pet-rock/rolling/rock-pet-animation-frames(22).png'))
        self.sprites.append(pg.image.load('art_assets/pet-rock/rolling/rock-pet-animation-frames(23).png'))
        self.sprites.append(pg.image.load('art_assets/pet-rock/rolling/rock-pet-animation-frames(24).png'))

        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        #self.image = pg.image.load("art_assets/pet-rock/rock-pet-animation-stand.png").convert_alpha()
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

        #status of player for animation
        self.status = 'art_assets/pet-rock/rock-pet-animation-stand.png'

    #def import_character_assets(self):
        #character_path = 'art_assets/pet-rock/rolling'
        #self.animations = {'rolling':[]}
        #for animation in self.animations.keys():
            #full_path = character_path + animation
            #self.animations[animation] = import_folder(full_path)

    #def get_status(self):
        #move these later
        #self.on_right = False
        #self.on_left = False
        #self.on_ceiling = False
        #self.on_ground = False
        #self.facing_right = True
        #if self.direction.x != 0:
           #self.status = 'rolling'

    #def animate(self):
        #animation = self.animations('rolling')
        #self.frame_index = self.animation_speed
        #if self.frame_index >= len(animation):
           #self.frame_index = 0
        #self.image = animation[int(self.frame_index)]

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
        self.current_sprite += 1

        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0

        self.image = self.sprites[self.current_sprite]
        #self.animate()
        #self.get_status()
