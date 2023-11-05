import pygame
from random import randint

from config import *


class LBlock:
    def __init__(self, x=None, y=None, size_x=None, size_y=None, color=None):
        if x is None:
            x = randint(0, SCREEN_SIZE_X - 4)
        if y is None:
            y = randint(0, SCREEN_SIZE_Y - 4)
        if size_x is None or size_y is None:
            size_x, size_y = 4, 4
        if color is None:
            color = (0, 128, 255)

        self.x = x
        self.y = y
        self.size_x = size_x
        self.size_y = size_y
        self.color = color

    def get_self(self):
        return self

    def random_move(self):
        self.x = randint(self.x-1, self.x+1)
        self.y = randint(self.y-1, self.y+1)
        from main import screen
        pygame.draw.rect(screen, self.color, pygame.Rect(self.x, self.y, self.size_x, self.size_y))
        