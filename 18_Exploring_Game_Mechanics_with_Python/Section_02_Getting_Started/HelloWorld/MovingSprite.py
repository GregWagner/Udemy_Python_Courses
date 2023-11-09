import pygame
from pygame.locals import *

pygame.init()

screen_width: int = 700
screen_height: int = 700

screen: pygame.Surface = pygame.display.set_mode((screen_width, screen_height), 0, 32)
pygame.display.set_caption("Display Butterfly")
screen.fill((0, 0, 0))

sprite1: pygame.Surface = pygame.image.load('./images/butterfly.png')
sprite1 = pygame.transform.scale(sprite1, (64, 64))
sprite_width: int = sprite1.get_width()
sprite_height: int = sprite1.get_height()

x: int = 0
y: int = 0

clock: int = pygame.time.Clock()
game_over: bool = False
while not game_over:
    dt = clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    pressed = pygame.key.get_pressed()
    if pressed[K_UP]:
        y -= 0.5 * dt
    if pressed[K_DOWN]:
        y += 0.5 * dt
    if pressed[K_RIGHT]:
        x += 0.5 * dt
    if pressed[K_LEFT]:
        x -= 0.5 * dt
    if pressed[K_SPACE]:
        x, y = 0, 0

    # x = screen_width - sprite_width if x > screen_width - sprite_width else x
    # x = 0 if x < 0 else x
    # y = screen_height - sprite_height if y > screen_height - sprite_height else y
    # y = 0 if y < 0 else y

    x = min(screen_width - sprite_width, x)
    x = max(0, x)
    y = min(screen_height - sprite_height, y)
    y = max(0, y)


    screen.fill((128, 0, 255))
    screen.blit(sprite1, (x, y))
    pygame.display.update()
pygame.quit()
