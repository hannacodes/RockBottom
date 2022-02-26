import pygame as pg, sys
from gameovermenu import game_over
from settings import *
from level import *
from level_tutorial import *

def level_1():
    pg.init()

    screen = pg.display.set_mode((screen_width, screen_height))
    clock = pg.time.Clock()
    level = Level(level_tutorial_map, screen)
    game_active = True
    game_over_event = False
    running = True
    while running: 
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if not game_active: 
                if ( event.type == pg.KEYDOWN and event.key == pg.K_SPACE ) or game_over_event:
                    game_active = True
                    level = Level(level_tutorial_map, screen)
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    running = False
        if game_active:    
            screen.fill((0,0,0))
            game_active = level.update()
        else:
            game_over_event = game_over(screen)
        pg.display.update()
        clock.tick(60)

if __name__ == '__main__':
    level_1()