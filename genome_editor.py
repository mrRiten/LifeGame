from random import randint


class GenomeEditor:
    def __init__(self, ref_object, strategy_list):
        self.ref_object = ref_object
        self.strategy_list = strategy_list

    def create_new_genome(self):
        genome_dict = {}
        for strategy in self.strategy_list:
            genome_element = strategy.active()
            genome_dict[genome_element[0]] = genome_element[1]

        recolor = self.comparison_genome(genome_dict)

        if recolor:
            genome_dict['color'] = self.generate_genome_color()
            print('new genome')
        else:
            genome_dict['color'] = self.ref_object.color
            print('new block')

        return genome_dict

    def generate_genome_color(self):
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

    def comparison_genome(self, new_genome_dict):
        pr_genome_dict = {'max_food': self.ref_object.max_food,
                          'outgo_food': self.ref_object.outgo_food,
                          'max_age': self.ref_object.max_age}

        for key in pr_genome_dict.keys():
            if pr_genome_dict.get(key) != new_genome_dict.get(key):
                return True

        return False
