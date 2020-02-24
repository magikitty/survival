# Import modules
import game_objects.animal as animal
import game_objects.player as player
import game_objects.player_setup as player_setup
import utilities.constants as constants
import utilities.dictionary as dictionary



# Initialize animal object
animal_1 = animal.Animal(constants.ANIMAL_1, constants.ATTACK_1)


# def player_survives():
#     action_animal = animal_1.get_attack()
#     print(constants.MESSAGE_ANIMAL_ATTACK, action_animal)
#     action_player = player.Player().actions

#     if dictionary.attack_response[action_animal] == action_player:
#         player_survives = True
#         print(constants.MESSAGE_PLAYER_SURVIVED_TRUE)
#     else:
#         player_survives = False
#         print(constants.MESSAGE_PLAYER_SURVIVED_FALSE)
#     return player_survives



player_setup.setPlayerNameFromInput()
# player_survives()
print("player name is", player.Player().name)
print("player does", player.Player().actions[0])
