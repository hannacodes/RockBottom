from cProfile import run
from turtle import bgcolor
import pygame as pg, pygame_gui as pgui, sys
clock = pg.time.Clock()
pg.init()
info = pg.display.Info()
bg_color = (123, 123, 123)

screen_width, screen_height = 1200, 900

def main_menu( screen ):
    manager = pgui.UIManager((screen_width, screen_height), 'theme.json')
    
    top = (screen_width/10) * 3
    left = screen_height/12
    width = screen_height/2
    height = screen_height/7

    t_layout_rect = pg.Rect(top, left, width, height)
    title = pgui.elements.UITextBox("Rock Bottom", relative_rect=t_layout_rect,
                                    manager=manager)

    running = True
    while running:
        screen.fill(bg_color)
        manager.update(60/1000.0)
        manager.draw_ui(screen)
        pg.display.update()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    running = False
            if event.type == pgui.UI_BUTTON_PRESSED:
                pass
            
            manager.process_events(event)
        
    clock.tick(60)


if __name__ == '__main__':
    pg.display.set_caption('Main Menu')
    screen = pg.display.set_mode((screen_width, screen_height),0,32)
    main_menu(screen)