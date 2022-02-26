import pygame as pg, sys
from settings import *
from level import *
from level_tutorial import *

def level_1():
    pg.init()

    screen = pg.display.set_mode((screen_width, screen_height))
    clock = pg.time.Clock()
    level = Level(level_tutorial_map, screen)
    game_active = True

    while True: 
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if not game_active: 
                if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                    game_active = True
                    level = Level(level_tutorial_map, screen)
        if game_active:    
            screen.fill((0,0,0))
            game_active = level.update()
        else:
            screen.fill((94, 129, 162)) 
        pg.display.update()
        clock.tick(60)

if __name__ == '__main__':
    level_1()