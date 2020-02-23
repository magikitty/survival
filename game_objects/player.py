from utilities import constants

# Class for the player game object
class Player(object):
    name = ""
    action = "defend"   # debugging


# TODO: move
def set_action_player(Player):
    action = get_input_action()
    if action == "1":
        print(constants.MESSAGE_SET_ACTION, constants.ACTION_1)
        return Player.actions[0]
    if action == "2":
        print(constants.MESSAGE_SET_ACTION, constants.ACTION_2)
        return Player.actions[1]


def get_input_action():
    print(constants.MENU_PLAYER_ACTIONS)
    input_valid = False
    while input_valid == False:
        input_action = input(constants.MESSAGE_INPUT_ACTION)
        if input_action == "1" or input_action == "2":
            return input_action
