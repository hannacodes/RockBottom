import pygame as pg

class Text(pg.sprite.Sprite):
    def __init__(self, num, pos):
        super().__init__()
        if(num == 0):
            self.image = pg.image.load("art_assets/font-images/pressarrow.png").convert_alpha()
            self.image = pg.transform.rotozoom(self.image, 0, 0.4)
        self.rect = self.image.get_rect(topleft = pos)

    def update(self, shift_x, shift_y):
        self.rect.x += shift_x
        self.rect.y += shift_y