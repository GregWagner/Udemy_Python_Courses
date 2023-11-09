import pygame as pg
from pygame.locals import *

screen_width: int = 800
screen_height: int = 600

pg.init()
screen: pg.Surface = pg.display.set_mode((screen_width, screen_height))
pg.display.set_caption("Breakin' Bricks")

bat: pg.Surface = pg.image.load('./images/paddle.png')
bat = bat.convert_alpha()
bat_rect = bat.get_rect()
bat_rect[1] = screen_height - 100

ball: pg.Surface = pg.image.load('./images/football.png')
ball = ball.convert_alpha()
ball_rect = ball.get_rect()
ball_start = (200, 200)
ball_speed = (3.0, 3.0)
ball_served: bool = False
sx, sy = ball_speed
ball_rect.topleft = ball_start

brick: pg.Surface = pg.image.load('./images/brick.png')
brick = brick.convert_alpha()
brick_rect = brick.get_rect()

bricks = []
brick_gap: int = 10
brick_rows: int = 5
brick_cols: int = screen_width // (brick_rect[2] + brick_gap)
side_gap: int = (screen_width - (brick_cols * (brick_rect[2] + brick_gap)) + brick_gap) // 2
for y in range(brick_rows):
    brick_y = y * (brick_rect[3] + brick_gap)
    for x in range(brick_cols):
        brick_x = x * (brick_rect[2] + brick_gap) + side_gap
        bricks.append((brick_x, brick_y))

clock: int = pg.time.Clock()
game_over: bool = False
while not game_over:
    dt: int = clock.tick(50)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            game_over = True

    pressed = pg.key.get_pressed()
    if pressed[K_LEFT]:
        bat_rect[0] -= 0.5 * dt
    if pressed[K_RIGHT]:
        bat_rect[0] += 0.5 * dt
    if pressed[K_SPACE]:
        ball_served = True

    # handle collision with paddle
    if bat_rect[0] <= ball_rect[0] <= bat_rect[0] + bat_rect[2] and \
        ball_rect[1] + ball_rect[3] >= bat_rect[1] and sy > 0:
        sy *= -1
        continue

    bat_rect[0] = min(screen_width - bat_rect[2], bat_rect[0])
    bat_rect[0] = max(0, bat_rect[0])

    if ball_served:
        ball_rect[0] += sx
        ball_rect[1] += sy

    # check for ball going off-screen
    if ball_rect[0] <= 0:
        sx *= -1
    if ball_rect[0] >= screen_width - ball_rect.width:
        sx *= -1
    if ball_rect[1] <= 0:
        sy *= -1
    if ball_rect[1] >= screen_height - ball_rect.height:
        # ball_served = False
        # ball_rect.topleft = ball_start
        sy *= -1

    screen.fill((0, 0, 0))
    for b in bricks:
        screen.blit(brick, b)

    screen.blit(bat, bat_rect)
    screen.blit(ball, ball_rect)
    pg.display.update()

pg.quit()
