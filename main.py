# Import modules
import game_objects.animal as animal
import game_objects.animal_setup as animal_setup
import game_objects.player as player
import game_objects.player_action as player_action
import game_objects.player_setup as player_setup
import utilities.constants as constants
import utilities.dictionary as dictionary

import json


def welcome_pc():
    print(constants.MESSAGE_WELCOME)
    player_setup.set_pc_name_from_input()
    print(constants.MESSAGE_GREET_PC_1, player.Player().name + constants.MESSAGE_GREET_PC_2)


def game_loop():
    pc_is_alive = True
    while pc_is_alive == True:
        # Get animal for encounter
        animal_in_encounter = animal_setup.get_random_animal()
        # Inform player of instantiated animal
        print(animal_in_encounter.name, constants.MESSAGE_ENCOUNTER_ANIMAL_NAME)

        # Get player input, check if survives encounter
        pc_survived_encounter = pc_survives_encounter(animal_in_encounter)

        if pc_survived_encounter == False:
            pc_is_alive = False
            print(constants.MESSAGE_GAME_OVER)
        else:
            print(constants.MESSAGE_ANOTHER_ANIMAL_APPROACHES)


# Get animal attack & player action, return whether player survives
def pc_survives_encounter(animal_encountered):
    attack_animal = animal_encountered.get_attack_random()
    print(constants.MESSAGE_ANIMAL_ATTACK, attack_animal)
    action_pc = player_action.set_action_player(player.Player())

    if dictionary.attack_response[attack_animal] == action_pc:
        pc_survives = True
        print(constants.MESSAGE_PLAYER_SURVIVED_TRUE)
    else:
        pc_survives = False
        print(constants.MESSAGE_PLAYER_SURVIVED_FALSE)
    return pc_survives


welcome_pc()
game_loop()
