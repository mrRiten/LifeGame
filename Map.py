import pygame
import numpy as np

from LBlock import LBlock


class Map:
    def __init__(self, x_size, y_size):
        self.map_array = np.zeros((y_size, x_size), dtype=int).tolist()
        self.list_blocks = []

    def set_position(self,  block_ref, block_x, block_y):
        delta_y = block_y
        for i in range(4):
            delta_x = block_x
            for i_ in range(4):
                self.map_array[delta_y][delta_x] = block_ref
                delta_x += 1
            delta_y += 1

    def add_block(self, block_ref):
        self.list_blocks.append(block_ref)

    def check_position(self, x, y):
        if self.map_array[y][x] != 0 or self.map_array[y+4][x] != 0 or self.map_array[y][x+4] != 0 or self.map_array[y+4][x+4] != 0:
            return False
        else:
            return True

    def draw_block(self, start_order):
        from main import screen
        for i in range(start_order):
            l_block = LBlock()
            if self.check_position(l_block.x, l_block.y):
                pygame.draw.rect(screen, l_block.color, pygame.Rect(l_block.x, l_block.y, l_block.size_x, l_block.size_y))
                self.set_position(l_block.get_self(), l_block.x, l_block.y)
                self.add_block(l_block.get_self())
        