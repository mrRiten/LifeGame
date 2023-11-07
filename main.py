import inspect

import pygame

from config import *
from LBlock import LBlockConstructor, l_blocks


clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((SCREEN_SIZE_X, SCREEN_SIZE_Y))
done = False

LBlockConstructor.create_block_start(l_blocks, 10)

while not done:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    l_blocks.draw(screen)
    l_blocks.update()

    pygame.display.update()
    pygame.display.flip()
    clock.tick(10)

