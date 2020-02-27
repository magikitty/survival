import utilities.lists as lists

import random


class Animal(object):
    def __init__(self, name):
        self.name = name
        # Inherited classes have different attack lists
        self.attacks = lists.animal_attacks
    def get_attack_random(self):
        attack_random = random.choice(self.attacks)
        return attack_random


class AnimalClaws(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)
        self.attacks = lists.animal_attacks_claws


class AnimalFlying(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)
        self.attacks = lists.animal_attacks_flying


class AnimalWater(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)
        self.attacks = lists.animal_attacks_water
