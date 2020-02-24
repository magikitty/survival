import random
import utilities.constants as constants


# Class for the mutant animal game object
class Animal(object):
    def __init__(self, name, attack):
        self.name = name
        self.attack = attack
    def get_attack(self):
        return self.attack


# class Animal(object):
#     def __init__(self, name):
#         self.name = name
#         self.attacks = ["stomp", "charge"]
#     def get_attack_random(self):
#         attack_random = random.choice(self.attacks)
#         print(constants.MESSAGE_ANIMAL_ATTACK, attack_random)
#         return attack_random
