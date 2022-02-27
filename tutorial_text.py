import pygame as pg

#class for text to be placed onto levels
#separate from tiles because doesn't detect collision
class Text(pg.sprite.Sprite):
    def __init__(self, num, pos):
        super().__init__()
        if(num == 0):
            self.image = pg.image.load("art_assets/font-images/pressarrow.png").convert_alpha()
            self.image = pg.transform.rotozoom(self.image, 0, 0.4)
        elif(num == 1):
            self.image = pg.image.load("art_assets/font-images/press-space.png").convert_alpha()
            self.image = pg.transform.rotozoom(self.image, 0, 0.5)
        elif(num == 2):
            self.image = pg.image.load("art_assets/font-images/warning.png").convert_alpha()
            self.image = pg.transform.rotozoom(self.image, 0, 0.5)
        elif(num == 3):
            self.image = pg.image.load("art_assets/font-images/bounce.png").convert_alpha()
            self.image = pg.transform.rotozoom(self.image, 0, 0.5)
        #for level 2
        elif(num == 4):
            self.image = pg.image.load("art_assets/font-images/the-end.png").convert_alpha()
            self.image = pg.transform.rotozoom(self.image, 0, 0.5)
        elif(num == 5):
            self.image = pg.image.load("art_assets/city-level/trust-sign.png").convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)

    def update(self, shift_x, shift_y):
        self.rect.x += shift_x
        self.rect.y += shift_y