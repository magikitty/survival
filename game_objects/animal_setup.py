import game_objects.animal as animal
import random
import utilities.constants as constants
import utilities.lists as lists


# Instantiates an Animal object with random name from list
def get_random_animal():
    num = random.randint(0, 2)
    if num == 0:
        animal_random = animal.Animal(random.choice(lists.list_animals))
    elif num == 1:
        animal_random = animal.AnimalWater(random.choice(lists.list_animals_water))
    else:
        animal_random = animal.AnimalFlying(random.choice(lists.list_animals_flying))
    return animal_random
