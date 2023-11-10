import pygame
from random import randint

from config import *
from GenomeEditor import GenomeEditor

l_blocks = pygame.sprite.Group()    # Main SpriteGroup for SpriteLBlock


class SpriteLBlock(pygame.sprite.Sprite):
    """
    Main Class for any SpriteLBlock
    """
    def __init__(self, x=None, y=None, size_x=None, size_y=None, color=None, group=None, genome=None):
        # dev settings
        super().__init__()
        if x is None:
            x = randint(0, SCREEN_SIZE_X - 4)
        if y is None:
            y = randint(0, SCREEN_SIZE_Y - 4)
        if size_x is None or size_y is None:
            size_x, size_y = 4, 4
        if color is None:
            color = (randint(0, 255), randint(0, 255), randint(0, 255))

        self.x = x
        self.y = y
        self.color = color
        self.add(group)
        self.image = pygame.Surface((size_x, size_y))   # set size
        self.image.fill(self.color)
        self.rect = self.image.get_rect(center=(self.x, self.y))    # set position

        self.max_food = 0
        self.outgo_food = 0
        self.max_age = 0

        if genome is None:
            # starter genome`s settings
            self.max_food = randint(1, 100)
            self.outgo_food = randint(1, 2)
            self.max_age = randint(10, 100)
        else:
            # ToDo recode this moment (optimization)
            if genome.get('max_food') is not None:
                self.max_food = genome.get('max_food')
            if genome.get('outgo_food') is not None:
                self.outgo_food = genome.get('outgo_food')
            if genome.get('max_age') is not None:
                self.max_age = genome.get('max_age')

        # game`s settings
        self.food = self.max_food / 2
        self.age = 0

    def update(self):
        self.one_step()
        self.die()
        self.random_move()
        self.up_food()
        self.create_child()

    #   action methods
    def random_move(self):
        self.x = randint(self.x-5, self.x+5)
        self.y = randint(self.y-5, self.y+5)
        self.rect = self.image.get_rect(center=(self.x, self.y))

    def up_food(self):
        self.food += 2

    def create_child(self):
        if self.food >= self.max_food:
            LBlockConstructor.create_block_child(self)
            self.food = self.max_food / 40

    def one_step(self):
        self.age += 1
        self.food -= self.outgo_food

    def die(self):
        if self.age >= self.max_age or self.food < 0:
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
    def create_block_child(ref_object):
        gen_editor = GenomeEditor(ref_object)
        genome = gen_editor.create_new_genome()
        try:
            SpriteLBlock(randint(ref_object.x-2, ref_object.x+2), randint(ref_object.y-2, ref_object.y+2),
                         color=genome.get('color'), group=l_blocks, genome=genome)
        except ValueError:
            pass
