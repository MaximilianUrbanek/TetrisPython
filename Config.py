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
window_width = 300
window_heigth = 600
block_size = 30
window_surface = pygame.display.set_mode((window_width, window_heigth))
pygame.display.set_caption("Tetris clone")

window_surface.fill(BLACK)
# Blocks


def drawGrid():
    for x in range(window_width):
        for y in range(window_heigth):
            rect = pygame.Rect(x * block_size, y * block_size,
                               block_size, block_size)
            pygame.draw.rect(window_surface, WHITE, rect, 1)




while True:
    drawGrid()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()


    #pygame.draw.rect(window_surface, RED, Game.tetris_shapes[1])
    pygame.display.update()
    clock.tick(500)



