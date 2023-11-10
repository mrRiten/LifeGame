from random import randrange, randint

from decorator import change_generation


# ToDo some problems with color
class GenomeEditor:
    def __init__(self, ref_object):
        self.ref_object = ref_object
        self.editor = 0

    def create_new_genome(self):
        # ToDo recode this method
        max_food = self.generate_genome_max_food()
        if max_food is None:
            max_food = self.ref_object.max_food
            self.editor -= 1

        outgo_food = self.generate_genome_outgo_food()
        if outgo_food is None:
            outgo_food = self.ref_object.outgo_food
            self.editor -= 1

        max_age = self.generate_genome_max_age()
        if max_age is None:
            max_age = self.ref_object.max_age
            self.editor -= 1

        color = self.generate_genome_color()
        if color is None:
            color = self.ref_object.color

        genome_dict = {'max_food': max_food,
                       'outgo_food': outgo_food,
                       'max_age': max_age,
                       'color': color
                       }
        return genome_dict

    @change_generation
    def generate_genome_max_food(self):
        new_max_food = self.ref_object.max_food + randrange(-1, 1, 1)
        self.editor += 1
        return new_max_food

    @change_generation
    def generate_genome_outgo_food(self):
        new_outgo_food = self.ref_object.outgo_food + randrange(-1, 1, 1)
        self.editor += 1
        return new_outgo_food

    @change_generation
    def generate_genome_max_age(self):
        new_outgo_food = self.ref_object.outgo_food + randrange(-1, 1, 1)
        self.editor += 1
        return new_outgo_food

    def generate_genome_color(self):
        if self.editor > 0:
            color = list(self.ref_object.color)
            for color_id in color:
                color_id += int(randrange(-10, 10, 10))
            color = tuple(color)
            color = (randint(0, 255), randint(0, 255), randint(0, 255))
            print(f'{self.ref_object.color} -> {color}')
            return color
