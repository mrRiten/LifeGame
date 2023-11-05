import pygame
import time

from Map import Map
from config import *
from LBlock import LBlock


clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((SCREEN_SIZE_X, SCREEN_SIZE_Y))
done = False

block_map = Map(SCREEN_SIZE_X+1, SCREEN_SIZE_Y+1)

block_map.draw_block(50)

while not done:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    for l_block in block_map.list_blocks:
        l_block.random_move()

    pygame.display.flip()
    clock.tick(60)
