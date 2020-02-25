import utilities.constants as constants
import utilities.dictionary as dictionary


def set_action_player(player_obj):
    print(constants.MENU_PLAYER_ACTIONS)
    while True:
        action = check_dict_for_input(input(constants.MESSAGE_INPUT_ACTION))
        if action != "":
            print(constants.MESSAGE_SET_ACTION, action)
            return action


def check_dict_for_input(input_action):
    if input_action in dictionary.player_input_action:
        return dictionary.player_input_action[input_action]
    else:
        return ""
