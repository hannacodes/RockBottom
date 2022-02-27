import pygame as pg, pygame_gui as pgui, sys
from pygame_gui.core import ObjectID
from main import level_1, level_2
clock = pg.time.Clock()
pg.init()

bg_color = (130, 95, 118)

screen_width, screen_height = 1200, 900


def winner1(screen, curr_level):
    manager = pgui.UIManager((screen_height, screen_width), 'menutheme.json')
    top = (screen_width/10) * 3
    left = screen_height/5
    width = screen_height/2
    height = screen_height/7

    t_layout_rect = pg.Rect(top, left, width, height)
    title = pgui.elements.UILabel( relative_rect=t_layout_rect, 
                                    text = 'You Win!',
                                    manager=manager )
    
    b1_layout_rect = pg.Rect(top, left+height+20, width, height)
    button1 = pgui.elements.UIButton(relative_rect=b1_layout_rect, text='Next Level', manager=manager)
    b2_layout_rect = pg.Rect(top, left+height*2+20, width, height)
    button2 = pgui.elements.UIButton(relative_rect=b2_layout_rect, text='Retry Level', manager=manager)
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
                    level_select(screen)
            if event.type == pgui.UI_BUTTON_PRESSED:
                if event.ui_element == button1:
                    level_2()
                if event.ui_element == button2: 
                    if curr_level == 1 :
                        update_str = level_1(screen)
                    elif curr_level == 2:
                        update_str = level_2(screen)
                    if(update_str == "Game Over"):
                        game_over(screen, curr_level)
                    if(update_str == "You Win"):
                        winner1(screen, curr_level)

                    running=False

                if event.ui_element == button3:
                    running = False 
                    level_select(screen)

            manager.process_events(event)
        clock.tick(60)

def game_over(screen, curr_level):
    manager = pgui.UIManager((screen_height, screen_width), 'menutheme.json')
    top = (screen_width/10) * 3
    left = screen_height/5
    width = screen_height/2
    height = screen_height/7

    t_layout_rect = pg.Rect(top, left, width, height)
    title = pgui.elements.UILabel( relative_rect=t_layout_rect, 
                                    text = 'You Died!',
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
                    if curr_level == 1:
                        update_str = level_1(screen)
                    elif curr_level == 2: 
                        update_str = level_2(screen)

                    if(update_str == "Game Over"):
                        game_over(screen, curr_level)
                    if(update_str == "You Win" ):
                        winner1(screen, curr_level)
                if event.ui_element == button2:
                    level_select(screen)
                    return False
            manager.process_events(event)
        clock.tick(60)

def level_select(screen):
    manager = pgui.UIManager((screen_height, screen_width), 'menutheme.json')
    layout_rect_1 = pg.Rect(screen_width/11 * 4 - screen_width/6, screen_height/6 * 3.9 - screen_width/4, screen_width/4, screen_width/4)
    layout_rect_2 = pg.Rect(screen_width/11 * 7.3 - screen_width/6, screen_height/6 * 3.9 - screen_width/4, screen_width/4, screen_width/4)

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
                    main_menu(screen)
            if event.type == pgui.UI_BUTTON_PRESSED:
                if event.ui_element == level1:
                    curr_level = 1
                    update_str = level_1(screen)
                    if(update_str == "Game Over"):
                        game_over(screen, curr_level)
                    if(update_str == "You Win" ):
                        winner1(screen, curr_level)
                if event.ui_element == level2:
                    curr_level = 2
                    print("button clicked")
                    update_str = level_2(screen)
                    if(update_str == "Game Over"):
                        game_over(screen, curr_level)
                    if(update_str == "You Win" ):
                        winner1(screen, curr_level)
            manager.process_events(event)
        clock.tick(60)


def help(screen):
    manager = pgui.UIManager((screen_height, screen_width), 'menutheme.json')
    manager.add_font_paths(font_name = 'dogica', regular_path = 'fonts/dogica.ttf', bold_path = '/font/dogicabold.ttf')
    manager.add_font_paths(font_name = 'dogicapixel', regular_path = 'fonts/dogicapixel.ttf', bold_path = '/font/dogicapixel.ttf')
    help = "<font face = dogica color = #FFFFFF size = 3>Temporary help method</font>"
    help_layout_rect = pg.Rect(screen_width/4, screen_height/12, ( screen_width/3 )* 2, screen_height/2)
    help = pgui.elements.UITextBox( help, relative_rect=help_layout_rect, manager=manager )
    exit_layout_rect = pg.Rect(screen_width/4, screen_height/12 + screen_height/2 + 10, screen_width/10, screen_height/14)
    exit = pgui.elements.UIButton(relative_rect=exit_layout_rect, text='Exit', manager=manager, object_id=ObjectID(object_id='#exit_button') )
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

    manager = pgui.UIManager((screen_width, screen_height), 'menutheme.json')
    top = (screen_width/10) * 3
    left = screen_height/5
    width = screen_height/2
    height = screen_height/7

    t_layout_rect = pg.Rect(top, left, width, height)
    title = pgui.elements.UILabel( relative_rect=t_layout_rect, 
                                    text = 'Rock Bottom',
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
                    pg.quit()
                    sys.exit()
            if event.type == pgui.UI_BUTTON_PRESSED:
                if event.ui_element == button1:
                    level_select(screen)
                if event.ui_element == button2:
                    help(screen)
                if event.ui_element == button3:
                    pg.quit()
                    sys.exit()

            manager.process_events(event)
        
    clock.tick(60)


if __name__ == '__main__':
    pg.display.set_caption('Rock Bottom')
    screen = pg.display.set_mode((screen_width, screen_height))
    main_menu(screen)