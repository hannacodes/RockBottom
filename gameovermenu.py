from cProfile import run
import pygame as pg, pygame_gui as pgui, sys
clock = pg.time.Clock()
pg.init()
info = pg.display.Info()
bg_color = (123, 123, 123)

screen_width, screen_height = 1200, 900

def game_over(screen):
    manager = pgui.UIManager((screen_height, screen_width), 'theme.json')
    top = (screen_width/10) * 3
    left = screen_height/5
    width = screen_height/2
    height = screen_height/7

    t_layout_rect = pg.Rect(top, left, width, height)
    title = pgui.elements.UITextBox( "<font face = 'verdana' color = '#ffffff' size = 7 >You died!</font>",
                                    relative_rect=t_layout_rect,
                                    manager=manager )
    
    b1_layout_rect = pg.Rect(top, left+height+20, width, height)
    button1 = pgui.elements.UIButton(relative_rect=b1_layout_rect, text='Try Again', manager=manager)
    b2_layout_rect = pg.Rect(top, left+height*2+20, width, height)
    button2 = pgui.elements.UIButton(relative_rect=b2_layout_rect, text='Exit', manager=manager)

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
                if event.ui_element == button1:
                    running = False
                    return True
                if event.ui_element == button2:
                    running = False
                    return False
            manager.process_events(event)
        clock.tick(60)