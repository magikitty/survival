# Import modules
from game_objects import player
from game_objects import animal
import constants
import dictionary

# Get player character name
def character_name():
    character_name = input(constants.MESSAGE_ENTER_NAME)
    return character_name

# Initialize game objects
player = player.Player(character_name())
animal_1 = animal.Animal(constants.ANIMAL_1)


def player_survives():
    action_animal = animal_1.get_attack_random()
    action_player = player.action()

    if dictionary.attack_response[action_animal] == action_player:
        player_survives = True
        print(constants.MESSAGE_PLAYER_SURVIVED_TRUE)
    else:
        player_survives = False
        print(constants.MESSAGE_PLAYER_SURVIVED_FALSE)
    return player_survives


player_survives()
