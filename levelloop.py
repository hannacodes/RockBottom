import pygame as pg, sys
from settings import *
from level import *
from level_tutorial import *
from tutorial_text import *
from level_city import *

clock = pg.time.Clock()

def level_1(screen):
    pg.init()
    
    level = Level(level_tutorial_map, screen, 1)
    #forest background for tutorial level
    forest_surf = pg.image.load("art_assets/forest-level/forest-level-background-altered1.png").convert_alpha()

    game_active = True
    win_condition = False
    running = True
    while running: 
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            #what to do when game over (game_active is not True)
            if not game_active: 
                if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                    game_active = True
                    level = Level(level_tutorial_map, screen, 1)
                    game_active = level.update()
                    win_condition = level.end_collide()
            #can escape using escape key
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    running = False
                    return ""
        #win condition when end flag is reached 
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

def level_2(screen):
    
    level = Level(level_city_map, screen, 2)
    #city level background
    city_surf = pg.image.load("art_assets/city-level/city-level-background.png").convert_alpha()
    city_surf = pg.transform.rotozoom(city_surf, 0, 3.5)

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
                    level = Level(level_tutorial_map, screen, 2)
                    game_active = level.update()
                    win_condition = level.end_collide()
            
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    running = False
                    return ""
        if win_condition: 
            running = False
            return "You Win"
        
        elif game_active:  
            screen.blit(city_surf, (0,0))
            game_active = level.update()
            win_condition = level.end_collide()
        elif not game_active and not win_condition:
             running = False
             return "Game Over"
        pg.display.update()
        clock.tick(60)
