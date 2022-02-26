import pygame as pg, sys
import pygame_gui as pgui
from settings import *
from level import *
from level_tutorial import *

def level_1():
    pg.init()

    screen = pg.display.set_mode((screen_width, screen_height))
    clock = pg.time.Clock()
    level = Level(level_tutorial_map, screen, 1)

    forest_surf = pg.image.load("art_assets/forest-level/forest-level-background.png").convert_alpha()
    forest_surf = pg.transform.rotozoom(forest_surf, 0, 3)

    game_active = True
    win_condition = False
    running = True
    while running: 
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if not game_active: 
                if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                    game_active = True
                    level = Level(level_tutorial_map, screen, 1)
                    game_active = level.update()
                    win_condition = level.end_collide()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    running = False
        if win_condition: 
            running = False
            return "You Win"
        elif game_active:    
            screen.blit(forest_surf, (0,0))
            game_active = level.update()
            win_condition = level.end_collide()
        elif not game_active and not win_condition:
             running = False
             return "Game Over"
        pg.display.update()
        clock.tick(60)

def level_2():
    pass

if __name__ == '__main__':
    level_1()