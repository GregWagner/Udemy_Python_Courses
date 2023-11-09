import pygame as pg

blocks = [
    [[1, 4, 7], [3, 4, 5]],         # stright
    [[1, 3, 4, 5, 7]],              # cross
    [[0, 1, 4, 5], [1, 3, 4, 6]],     # two on two 1
    [[1, 2, 3, 4], [0, 3, 4, 7]],   # two on two 2
    [[0, 1, 3, 6], [0, 1, 2, 5], [2, 5, 7, 8], [3, 6, 7, 8]], # l1
    [[1, 2, 5, 8], [5, 6, 7, 8], [0, 3, 6, 7], [0, 1, 2, 3]], # l2
    [[4, 6, 7, 8], [0, 3, 4, 6], [0, 1, 2, 4], [2, 4, 5, 8]], # 1 on 3
]

class Block:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.type = 0
        self.rotation = 0

    def shape(self):
        return blocks[self.type][self.rotation]

def draw_block():
    for y in range(3):
        for x in range(3):
            if y * 3 + x in block.shape():
                pg.draw.rect(screen, (255, 255, 255),
                [(x + block.x) * grid_size + x_gap + 1,
                 (y + block.y) * grid_size + y_gap + 1,
                 grid_size - 2, grid_size - 2])


def draw_grid():
    for row in range(rows):
        row_position = row * grid_size + x_gap
        for col in range(cols):  # cols
            pg.draw.rect(screen, (100, 100, 100),
                             [row_position, col * grid_size + y_gap, grid_size, grid_size], 1)


grid_size = 30
pg.init()
screen = pg.display.set_mode((800, 800))
pg.display.set_caption("Tetris")

cols = screen.get_width() // grid_size
rows = screen.get_height() // grid_size
x_gap = (screen.get_width() - cols * grid_size) // 2
y_gap = (screen.get_height() - rows * grid_size) // 2

game_over = False
block = Block(5, 6)
while not game_over:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            game_over = True

    screen.fill((0, 0, 0))
    draw_grid()
    draw_block()
    pg.display.update()

pg.quit()
