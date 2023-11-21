from random import randrange

from decorator import change_generation


class DefaultStrategy:
    def __init__(self, ref_object):
        self.ref_object = ref_object
        self.__name__ = 'DefaultStr'
        self.default_genome = None

    def active(self):
        output = self.generate_genome()
        if output is None:
            output = self.default_genome
        return self.__name__, output

    @change_generation
    def generate_genome(self):
        pass


class GenerateGenomeMaxFood(DefaultStrategy):
    def __init__(self, ref_object):
        DefaultStrategy.__init__(self, ref_object)
        self.__name__ = 'max_food'
        self.default_genome = self.ref_object.max_food

    @change_generation
    def generate_genome(self):
        new_max_food = self.ref_object.max_food + randrange(-1, 1, 1)
        return new_max_food


class GenerateGenomeOutgoFood(DefaultStrategy):
    def __init__(self, ref_object):
        DefaultStrategy.__init__(self, ref_object)
        self.__name__ = 'outgo_food'
        self.default_genome = self.ref_object.outgo_food

    @change_generation
    def generate_genome(self):
        new_outgo_food = self.ref_object.outgo_food + randrange(-1, 1, 1)
        return new_outgo_food


class GenerateGenomeMaxAge(DefaultStrategy):
    def __init__(self, ref_object):
        DefaultStrategy.__init__(self, ref_object)
        self.__name__ = 'max_age'
        self.default_genome = self.ref_object.max_age

    @change_generation
    def generate_genome(self):
        new_max_age = self.ref_object.max_age + randrange(-1, 1, 1)
        return new_max_age


class GenerateGenomeLinker:
    def __init__(self, ref_object):
        self.strategy_list = [
            GenerateGenomeMaxFood(ref_object),
            GenerateGenomeOutgoFood(ref_object),
            GenerateGenomeMaxAge(ref_object),
                              ]


