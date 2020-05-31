import os
import pygame
import Game


os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"

pygame.init()
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)
BLACK = (  0,   0,   0)


# Window settings
window_width = 800
window_heigth = 700
game_width = 300
game_heigth = 600
block_size = 30
window_surface = pygame.display.set_mode((window_width, window_heigth), 0, 32)
pygame.display.set_caption("Tetris clone")
left_corner_x = (window_width - game_width) // 2
left_corner_y = window_heigth - game_heigth

window_surface.fill(BLACK)
title = pygame.font.SysFont('arial', bold=1, size=50).render('TETRIS', 1, RED)
window_surface.blit(title, (left_corner_x + game_width / 2 - (title.get_width() / 2), 30))

# Blocks
LINE = pygame.Rect(0, 0, 100, 100)


def drawGrid():
    for x in range(game_width):
        for y in range(game_heigth):
            rect = pygame.Rect(x * block_size, y * block_size, block_size, block_size)
            pygame.draw.rect(window_surface, WHITE, rect, 1)

while True:
    drawGrid()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()



    pygame.display.update()
    clock.tick(20000)



