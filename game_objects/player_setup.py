import utilities.constants
import game_objects.player


# print given message, return player input
def playerInputFromMessage(message):
    return input(message)


def setPlayerNameFromInput():
    name = playerInputFromMessage(utilities.constants.MESSAGE_ENTER_NAME)
    game_objects.player.Player.name = name