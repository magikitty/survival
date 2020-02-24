import random
import utilities.constants as constants

animal_attacks = [constants.ATTACK_1, constants.ATTACK_2]   # debugging


class Animal(object):
    def __init__(self, name):
        self.name = name
        self.attacks = animal_attacks
    def get_attack_random(self):
        attack_random = random.choice(self.attacks)
        return attack_random
