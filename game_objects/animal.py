import random
import utilities.constants as constants
import utilities.lists as lists


class Animal(object):
    def __init__(self, name):
        self.name = name
        self.attacks = lists.animal_attacks
    def get_attack_random(self):
        attack_random = random.choice(self.attacks)
        return attack_random
