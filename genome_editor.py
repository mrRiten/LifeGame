from random import randrange, randint

from decorator import change_generation

# ToDo: Create a method for comparison genome


class GenomeEditor:
    def __init__(self, ref_object):
        self.ref_object = ref_object
        self.editor = 0

    def create_new_genome(self):
        # ToDo recode this method use pattern Strategy

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
            color_old = self.ref_object.color
            color = []
            for i in range(len(color_old)):
                color_code = color_old[i] + randint(-10, 10)
                if color_code > 255:
                    color_code = 255
                if color_code < 0:
                    color_code = 0
                color.append(color_code)

            color = tuple(color)
            print(f'{self.ref_object.color} -> {color}')
            return color
