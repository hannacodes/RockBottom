import pygame as pg, pygame_gui as pgui, sys
from main import level_1
clock = pg.time.Clock()
pg.init()
info = pg.display.Info()
bg_color = (123, 123, 123)

screen_width, screen_height = 1200, 900

def level_select(screen):
    manager = pgui.UIManager((screen_height, screen_width), 'theme.json')
    layout_rect_1 = pg.Rect(screen_width/3 - screen_width/6, screen_height/2 - screen_width/4, screen_width/4, screen_width/4)
    layout_rect_2 = pg.Rect((screen_width/3)*2 - screen_width/6, screen_height/2 - screen_width/4, screen_width/4, screen_width/4)

    level1 = pgui.elements.UIButton(relative_rect=layout_rect_1, text='Level One', manager=manager)
    level2 = pgui.elements.UIButton(relative_rect=layout_rect_2, text='Level Two', manager=manager)

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
                if event.ui_element == level1:
                    level_1()
                if event.ui_element == level2:
                    pass
            manager.process_events(event)
        clock.tick(60)


def help(screen):
    manager = pgui.UIManager((screen_height, screen_width))
    help = "Temporary help method"
    help_layout_rect = pg.Rect(screen_width/4, screen_height/12, ( screen_width/3 )* 2, screen_height/2)
    help = pgui.elements.UITextBox( help, relative_rect=help_layout_rect, manager=manager )
    exit_layout_rect = pg.Rect(screen_width/4, screen_height/12 + screen_height/2, screen_width/10, screen_height/12)
    exit = pgui.elements.UIButton(relative_rect=exit_layout_rect, text='Exit', manager=manager)
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
                if event.ui_element == exit:
                    running = False
            
            manager.process_events(event)

def main_menu( screen ):

    manager = pgui.UIManager((screen_width, screen_height))
    manager.add_font_paths(font_name = 'dogica', regular_path = '/fonts/dogica.ttf', bold_path = '/font/dogicabold.ttf')
    manager.add_font_paths(font_name = 'dogicapixel', regular_path = '/fonts/dogicapixel.ttf', bold_path = '/font/dogicapixel.ttf')
    top = (screen_width/10) * 3
    left = screen_height/5
    width = screen_height/2
    height = screen_height/7

    t_layout_rect = pg.Rect(top, left, width, height)
    title = pgui.elements.UITextBox( "<font face = 'verdana' color = '#ffffff' size = 7 >Rock Bottom</font>",
                                    relative_rect=t_layout_rect,
                                    manager=manager )
    
    b1_layout_rect = pg.Rect(top, left+height+20, width, height)
    button1 = pgui.elements.UIButton(relative_rect=b1_layout_rect, text='Play Game', manager=manager)
    b2_layout_rect = pg.Rect(top, left+height*2+20, width, height)
    button2 = pgui.elements.UIButton(relative_rect=b2_layout_rect, text='Help', manager=manager)
    b3_layout_rect = pg.Rect(top, left+height*3+20, width, height)
    button3 = pgui.elements.UIButton(relative_rect=b3_layout_rect, text='Exit', manager=manager)

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
                    level_select(screen)
                if event.ui_element == button2:
                    help(screen)
                if event.ui_element == button3:
                    running = False

            manager.process_events(event)
        
    clock.tick(60)


if __name__ == '__main__':
    pg.display.set_caption('Main Menu')
    screen = pg.display.set_mode((screen_width, screen_height),0,32)
    main_menu(screen)