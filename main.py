import pygame

from config import *
from LBlock import LBlockConstructor, l_blocks


clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((SCREEN_SIZE_X, SCREEN_SIZE_Y))
active = False       # Process of game

LBlockConstructor.create_block_start(l_blocks, 50)  # Create start blocks

while not active:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            active = True

    l_blocks.draw(screen)
    l_blocks.update()   # Update blocks

    pygame.display.update()
    pygame.display.flip()
    clock.tick(10)

