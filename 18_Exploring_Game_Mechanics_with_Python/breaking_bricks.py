import pygame as pg
from pygame.locals import (K_RIGHT, K_LEFT, K_SPACE)

pg.init()
screen = pg.display.set_mode((800, 600))
pg.display.set_caption("Breakin' Bricks")

bat = pg.image.load('./images/paddle.png').convert_alpha()
bat_rect = bat.get_rect()
bat_rect.y = screen.get_height() - 100

ball = pg.image.load('./images/football.png').convert_alpha()
ball_rect = ball.get_rect()
ball_start = (200, 200)
ball_speed = (3.0, 3.0)
ball_served = False
sx, sy = ball_speed
ball_rect.topleft = ball_start

brick = pg.image.load('./images/brick.png').convert_alpha()
brick_rect = brick.get_rect()

bricks = []
brick_rows = 5
brick_gap = 10
brick_col = screen.get_width() // (brick_rect.width + brick_gap)
side_gap = (screen.get_width() - (brick_rect.width + brick_gap) * brick_col + brick_gap) // 2

for y in range(brick_rows):
    brick_y = y * (brick_rect[3] + brick_gap)
    for x in range(brick_col):
        brick_x = x * (brick_rect.width + brick_gap) + side_gap
        bricks.append((brick_x, brick_y))

clock = pg.time.Clock()

game_over = False
while not game_over:
    dt = clock.tick(50)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            game_over = True

    # Handle keyboad events
    pressed = pg.key.get_pressed()
    if pressed[K_RIGHT]:
        bat_rect.x += 0.5 * dt
    elif pressed[K_LEFT]:
        bat_rect.x -= 0.5 * dt
    elif pressed[K_SPACE]:
        ball_served = True

    # Handle the bat
    if bat_rect.x > screen.get_width() - bat_rect.width:
        bat_rect.x = screen.get_width() - bat_rect.width
    elif bat_rect.x < 0:
        bat_rect.x = 0

    # Handle the ball
    if ball_served:
        ball_rect.x += sx
        ball_rect.y += sy

    # Check for collision with paddle
    if bat_rect.x + bat_rect.width >= ball_rect.x >= bat_rect.x and \
            ball_rect.y >= bat_rect.y - bat_rect.height and sy > 0:
        sy *= -1.1
        sx *= 1.1
        continue

    delete_brick = None
    for b in bricks:
        bx, by = b
        if bx <= ball_rect.x <= bx + bat_rect.width and \
           by < ball_rect.y <= by + bat_rect.height:
            delete_brick = b

            if ball_rect.x <= bx + 2 or ball_rect.x >= bx + brick_rect.width - 2:
                sx *= -1
            elif ball_rect.y <= by + 2 or ball_rect.y >= by + brick_rect.height - 2:
                sy *= -1
            break
    if delete_brick is not None:
        bricks.remove(delete_brick)

    # Right
    if ball_rect.x >= screen.get_width() - ball_rect.width:
        ball_rect.x = screen.get_width() - ball_rect.width
        sx *= -1
    # Left
    elif ball_rect.x <= 0:
        ball_rect.x = 0
        sx *= -1
    # Bottom
    if ball_rect.y >= screen.get_height() - ball_rect.height:
        ball_served = False
        sx, sy = ball_speed
        ball_rect.topleft = ball_start
    # Top
    elif ball_rect.y <= 0:
        ball_rect.y = 0
        sy *= -1

    # draw to the screen
    screen.fill((0, 0, 0))
    for b in bricks:
        screen.blit(brick, b)

    screen.blit(bat, bat_rect)
    screen.blit(ball, ball_rect)

    pg.display.update()

pg.quit()