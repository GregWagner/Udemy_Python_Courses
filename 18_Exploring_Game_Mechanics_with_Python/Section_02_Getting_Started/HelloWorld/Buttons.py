import pygame as pg
pg.init()

screen_width: int = 500
screen_height: int = 500

screen: pg.Surface = pg.display.set_mode((screen_width, screen_height), 0, 32)
pg.display.set_caption('Making Buttons')

text_color = (255, 255, 255)
button_color = (0, 00, 170)
button_over_color = (255, 50, 50)

button_width: int = 100
button_height: int = 50
button_rect = [(screen_width - button_width) / 2,
               (screen_height - button_height) / 2,
               button_width, button_height]
button_font = pg.font.SysFont('Arial', 20)
button_text = button_font.render('Quit', True, text_color)

x: int = 0
y: int = 0

game_over: bool = False
while not game_over:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            game_over = True
        if event.type == pg.MOUSEBUTTONDOWN:
            x, y = event.pos
            if button_rect[0] <= x <= button_rect[0] + button_width and \
               button_rect[1] <= y <= button_rect[1] + button_height:
                game_over = True
        if event.type == pg.MOUSEMOTION:
            x, y = event.pos

    screen.fill((100, 100, 100))
    if button_rect[0] <= x <= button_rect[0] + button_width and \
            button_rect[1] <= y <= button_rect[1] + button_height:
        pg.draw.rect(screen, button_over_color, button_rect)
    else:
        pg.draw.rect(screen, button_color, button_rect)
    screen.blit(button_text,
                (button_rect[0] + (button_width - button_text.get_width()) / 2,
                 button_rect[1] + (button_height - button_text.get_height()) / 2))
    pg.display.update()

pg.quit()

