import random

# Class for the mutant animal game object
class Animal(object):
    def __init__(self, name):
        self.name = name
        self.attacks = ["stomp", "charge"]
    def get_attack_random(self):
        attack_random = random.choice(self.attacks)
        print(attack_random)
        return attack_random


moophant = Animal("Moophant")
moophant.get_attack_random()
