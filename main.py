import pygame as pg, sys

pg. init()

screen_width = 1200
screen_height = 900

screen = pg.display.set_mode((screen_width, screen_height))
clock = pg.time.Clock()

while True: 
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        
    screen.fill((0,0,0))

    pg.display.update()
    clock.tick(60)