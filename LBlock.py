import pygame
from random import randint

from config import *

l_blocks = pygame.sprite.Group()    # Main SpriteGroup for SpriteLBlock


class SpriteLBlock(pygame.sprite.Sprite):
    """
    Main Class for any SpriteLBlock
    """
    def __init__(self, x=None, y=None, size_x=None, size_y=None, color=None, group=None):
        # dev settings
        super().__init__()
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
        self.color = color
        self.add(group)
        self.image = pygame.Surface((size_x, size_y))   # set size
        self.image.fill(self.color)
        self.rect = self.image.get_rect(center=(self.x, self.y))    # set position

        # game`s settings
        self.food = 0
        self.age = 0

        # genome`s settings
        self.max_food = randint(1, 4)
        self.max_age = randint(10, 100)

    def update(self):
        self.one_step()
        self.die()
        self.random_move()
        self.up_food()
        self.create_child()

    def random_move(self):
        self.x = randint(self.x-5, self.x+5)
        self.y = randint(self.y-5, self.y+5)
        self.rect = self.image.get_rect(center=(self.x, self.y))

    def up_food(self):
        self.food += 0.1

    def create_child(self):
        if self.food >= self.max_food:
            LBlockConstructor.create_block_child(self.x, self.y)
            self.food = 0

    def one_step(self):
        self.age += 1

    def die(self):
        if self.age >= self.max_age:
            self.kill()


class LBlockConstructor:
    """
    Construct the LBlock with correct sittings
    """
    @staticmethod
    def create_block_start(group_name, quantity):   # only with start
        for i in range(quantity):
            SpriteLBlock(randint(4, SCREEN_SIZE_X), randint(4, SCREEN_SIZE_Y), group=group_name)

    @staticmethod
    def create_block_child(parent_x, parent_y):
        try:
            SpriteLBlock(randint(parent_x-2, parent_x+2), randint(parent_y-2, parent_y+2), group=l_blocks)
        except ValueError:
            pass
