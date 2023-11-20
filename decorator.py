from random import randint

from config import change_generation_percent


def change_generation(func):
    def wrapper(*args):
        change = randint(1, 100)
        if change <= change_generation_percent:
            return func(*args)
    return wrapper
