import os
import pygame

SET_CAPTION = pygame.display.set_caption("Tetris clone")
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"

pygame.init()
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)


# Window settings
WINDOW_WIDTH = 600
WINDOW_HEIGTH = 1200
WINDOW_SURFACE = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGTH), 0, 32)

# Blocks
LINE = pygame.Rect(0, 0, 100, 100)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    WINDOW_SURFACE.fill(BLUE)
    WINDOW_SURFACE.fill(RED, LINE)
    pygame.display.update()
    clock.tick(20000)

