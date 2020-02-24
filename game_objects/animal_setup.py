import game_objects.animal as animal
import random
import utilities.constants as constants

list_animals = [constants.ANIMAL_1, constants.ANIMAL_2]   # debugging


# Instantiates an Animal object with random name from list
def getRandomAnimal():
    animal_random = animal.Animal(random.choice(list_animals))
    return animal_random
