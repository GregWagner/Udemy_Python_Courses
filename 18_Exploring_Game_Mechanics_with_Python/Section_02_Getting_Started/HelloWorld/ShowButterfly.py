import pygame

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

game_over: bool = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    screen.blit(sprite1, ((screen_width / 2) - (sprite_width / 2), (screen_height / 2 - sprite_height / 1)))
    pygame.display.update()
pygame.quit()
