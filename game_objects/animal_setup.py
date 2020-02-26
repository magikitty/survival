import game_objects.animal as animal
import random
import utilities.constants as constants
import utilities.lists as lists


# Instantiates an Animal object with random name from list
def get_random_animal():
    animal_random = animal.Animal(random.choice(lists.list_animals))
    return animal_random
