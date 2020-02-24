# Import modules
import game_objects.animal as animal
import game_objects.player as player
import game_objects.player_action as player_action
import game_objects.player_setup as player_setup
import utilities.constants as constants
import utilities.dictionary as dictionary


# Get player name and greet player
def welcomePlayer():
    print(constants.MESSAGE_WELCOME)
    player_setup.setPlayerNameFromInput()
    print("Hello,", player.Player().name + "! Get ready to play!\n")


# Initialize animal object
animal_1 = animal.Animal(constants.ANIMAL_1, constants.ATTACK_1)


def gameLoop():
    player_is_alive = True
    while player_is_alive == True:
        # Get animal for encounter
        # Inform player of instantiated animal
        player_survives_encounter = player_survives()

        if player_survives_encounter == False:
            player_is_alive = False
            print(constants.MESSAGE_GAME_OVER)
        else:
            print(constants.MESSAGE_ANOTHER_ANIMAL_APPROACHES)


def player_survives():
    action_animal = animal_1.get_attack()
    print(constants.MESSAGE_ANIMAL_ATTACK, action_animal)
    action_player = player_action.set_action_player(player.Player())

    if dictionary.attack_response[action_animal] == action_player:
        player_survives = True
        print(constants.MESSAGE_PLAYER_SURVIVED_TRUE)
    else:
        player_survives = False
        print(constants.MESSAGE_PLAYER_SURVIVED_FALSE)
    return player_survives


welcomePlayer()
gameLoop()
