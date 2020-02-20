# Import modules
from game_objects import player
from game_objects import animal
import dictionary

# Initialize game objects
test_player = player.Player("Sally")
moophant = animal.Animal("Moophant")


# Test simplified gameloop
def player_survives():
    action_animal = moophant.get_attack_random()
    action_player = test_player.set_action_player()

    if dictionary.attack_response[action_animal] == action_player:
        player_survives = True
    else:
        player_survives = False
    print("Player survived is", player_survives)
    return player_survives


player_survives()
