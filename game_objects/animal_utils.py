import game_objects.animal as animal
import utilities.lists as lists

import random


# Instantiates an Animal object with random name from list
def get_random_animal():
    num = random.randint(0, 3)
    if num == 0:
        animal_random = animal.Animal(random.choice(lists.list_animals))
    elif num == 1:
        animal_random = animal.AnimalClaws(random.choice(lists.list_animals_claws)) 
    elif num == 2:
        animal_random = animal.AnimalFlying(random.choice(lists.list_animals_flying))
    else:
        animal_random = animal.AnimalWater(random.choice(lists.list_animals_water))
    return animal_random
