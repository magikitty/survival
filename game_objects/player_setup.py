import utilities.constants as constants
import game_objects.player as player


def setPlayerNameFromInput():
    name = input(constants.MESSAGE_ENTER_NAME)
    player.Player.name = name
