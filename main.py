import pygame as pg, sys
from settings import *
from level import *
pg. init()

screen = pg.display.set_mode((screen_width, screen_height))
clock = pg.time.Clock()
level = Level(level_map, screen)

while True: 
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        
    screen.fill((0,0,0))
    level.update()

    pg.display.update()
    clock.tick(60)