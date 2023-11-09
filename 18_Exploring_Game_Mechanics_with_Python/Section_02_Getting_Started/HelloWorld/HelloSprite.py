import pygame

pygame.init()

screen_width: int = 800
screen_height: int = 400

screen: pygame.Surface = pygame.display.set_mode((screen_width, screen_height), 0, 32)
pygame.display.set_caption("Display Sprite")
screen.fill((0, 0, 0))

sprite1: pygame.Surface = pygame.image.load('./images/football.png')

game_over: bool = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    screen.blit(sprite1, (screen_width / 2 - 16, 16 + screen_height / 2 - 16))
    pygame.display.update()
pygame.quit()
