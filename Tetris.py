import pygame as pg

# Window settings
window_width = 400
window_heigth = 800
block_size = 40
rows = window_width // block_size
cols = window_heigth // block_size

# Grid
grid = [0] * rows * cols

# Pictures
pic = []
for n in range(8):
    pic.append(pg.transform.scale(pg.image.load("Pictures/{}.png".format(n)), (block_size, block_size)))


pg.init()
window_surface = pg.display.set_mode([window_width, window_heigth])
pg.display.set_caption("Tetris")

# Shapes, 4 Zahlen pro Zeile um Formen zu definieren
shape_c = [[0,1,1,0,
           0,1,1,0,
           0,0,0,0,
           0,0,0,0]]
shape_t = [[2,2,2,0,
           0,2,0,0,
           0,0,0,0,
           0,0,0,0],
           [0,2,0,0,
            0,2,2,0,
            0,2,0,0,
            0,0,0,0],
           [0,2,0,0,
            2,2,2,0,
            0,0,0,0,
            0,0,0,0],
           [0,2,0,0,
            2,2,0,0,
            0,2,0,0,
            0,0,0,0]]
shape_s = [[0,3,3,0,
            3,3,0,0,
            0,0,0,0,
            0,0,0,0],
           [0,3,0,0,
            0,3,3,0,
            0,0,3,0,
            0,0,0,0]]
shape_z = [[0,4,4,0,
            0,0,4,4,
            0,0,0,0,
            0,0,0,0],
           [0,0,4,0,
            0,4,4,0,
            0,4,0,0,
            0,0,0,0]]
shape_i = [[5,5,5,5,
            0,0,0,0,
            0,0,0,0,
            0,0,0,0],
           [0,5,0,0,
            0,5,0,0,
            0,5,0,0,
            0,5,0,0]]
shape_l2 = [[0,6,0,0,
           0,6,0,0,
           0,6,6,0,
           0,0,0,0],
           [0,0,6,0,
            6,6,6,0,
            0,0,0,0,
            0,0,0,0],
           [0,6,6,0,
            0,0,6,0,
            0,0,6,0,
            0,0,0,0],
           [6,6,6,0,
            6,0,0,0,
            0,0,0,0,
            0,0,0,0]]
shape_l1 = [[0,0,7,0,
             0,0,7,0,
             0,7,7,0,
             0,0,0,0],
            [7,7,7,0,
             0,0,7,0,
             0,0,0,0,
             0,0,0,0],
            [0,7,7,0,
             0,7,0,0,
             0,7,0,0,
             0,0,0,0],
            [0,7,0,0,
             0,7,7,7,
             0,0,0,0,
             0,0,0,0]]
shapes = [shape_c, shape_i, shape_s, shape_t, shape_z, shape_l1, shape_l2]

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            quit()

    window_surface.fill((0,0,0))
    for n, m in enumerate(grid):
        if m > 0:
            x = n % rows * block_size
            y = n // rows * block_size
            window_surface.blit(pic[m], (x,y))
    pg.display.flip()

pg.quit()