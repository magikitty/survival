import utilities.constants as constants
import game_objects.player as player


def set_pc_name_from_input():
    name = input(constants.MESSAGE_ENTER_NAME)
    player.Player.name = name


def add_point_pc():
    player.Player.points += 1
