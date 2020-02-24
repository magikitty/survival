import utilities.constants as constants
import game_objects.player as player


# print given message, return player input
def playerInputFromMessage(message):
    return input(message)


def setPlayerNameFromInput():
    name = playerInputFromMessage(constants.MESSAGE_ENTER_NAME)
    player.Player.name = name