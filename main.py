# Import modules
from game_objects import animal
from game_objects import player_setup
import game_objects.player
from utilities import constants
from utilities import dictionary



# Initialize game objects
# player = player.Player(character_name())
# player_char = player.Player()
# player_char.action("sally")
animal_1 = animal.Animal(constants.ANIMAL_1, constants.ATTACK_1)


# def player_survives():
#     action_animal = animal_1.get_attack()
#     print(constants.MESSAGE_ANIMAL_ATTACK, action_animal)
#     # action_player = player.action()

#     if dictionary.attack_response[action_animal] == action_player:
#         player_survives = True
#         print(constants.MESSAGE_PLAYER_SURVIVED_TRUE)
#     else:
#         player_survives = False
#         print(constants.MESSAGE_PLAYER_SURVIVED_FALSE)
#     return player_survives


# player_survives()



player_setup.setPlayerNameFromInput()
print("player name is", game_objects.player.Player().name)
print("player does", game_objects.player.Player().action)
