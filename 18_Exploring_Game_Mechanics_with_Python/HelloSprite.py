import pygame
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((800, 600), 0, 32)
pygame.display.set_caption("Hello Pygame")
screen.fill((0, 0, 0))

sprite1 = pygame.image.load('./Images/football.png')
# rescale the sprite
sprite1 = pygame.transform.scale(sprite1, (64, 64))
sprite_width = sprite1.get_width()
sprite_height = sprite1.get_height()

text_color = (255, 255, 255)
button_color = (0, 0, 170)
button_over_color = (255, 50, 50)
button_width = 100
button_height = 50
button_rect = [screen.get_width() // 2 - button_width // 2,
               screen.get_height() // 2 - button_height // 2.,
               button_width, button_height]
button_font = pygame.font.SysFont('Arial', 20)
button_text = button_font.render('Quit', True, text_color)


game_over = False
x, y = 0, 0
clock = pygame.time.Clock()

while not game_over:
    dt = clock.tick(100)
    for event in pygame.event.get():
        button_color = (0, 0, 170)
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if button_rect[0] <= x <= button_rect[0] + button_rect[2] and \
               button_rect[1] <= y <= button_rect[1] + button_rect[3]:
                game_over = True
        elif event.type == pygame.MOUSEMOTION:
            #x, y = event.pos[0] - sprite_width / 2, event.pos[1] - sprite_height / 2
            x, y = event.pos
            if button_rect[0] <= x <= button_rect[0] + button_rect[2] and \
               button_rect[1] <= y <= button_rect[1] + button_rect[3]:
                button_color = button_over_color

        pressed = pygame.key.get_pressed()

    if pressed[K_UP]:
        y -= 0.5 * dt
    if pressed[K_DOWN]:
        y += 0.5 * dt
    if pressed[K_LEFT]:
        x -= 0.5 * dt
    if pressed[K_RIGHT]:
        x += 0.5 * dt
    if pressed[K_SPACE]:
        x, y = 0, 0

    if x > screen.get_width() - sprite_width:
        x = screen.get_width() - sprite_width
    elif x < 0:
        x = 0

    if y > screen.get_height() - sprite_height:
        y = screen.get_height() - sprite_height
    elif y < 0:
        y = 0
    # draw in center of screen
    #screen.blit(sprite1, (screen.get_width() / 2 - sprite_width / 2,
    #                     screen.get_height() / 2 - sprite_height / 2))
    screen.fill((100, 100, 100))
    pygame.draw.rect(screen, button_color, button_rect)
    screen.blit(button_text, (button_rect[0] + (button_width - button_text.get_width()) // 2,
                              button_rect[1] + (button_height - button_text.get_height()) // 2))
    screen.blit(sprite1, (x, y))
    pygame.display.update()
pygame.quit()