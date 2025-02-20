# Import modules
import game_objects.animal as animal
import game_objects.animal_utils as animal_utils
import game_objects.player as player
import game_objects.player_action as player_action
import game_objects.player_utils as player_utils
import utilities.constants as constants
import utilities.dictionary as dictionary


def welcome_pc():
    print(constants.MESSAGE_WELCOME)
    print(constants.MESSAGE_GAME_INFO)
    player_utils.set_pc_name_from_input()
    print(constants.MESSAGE_GREET_HELLO, player.Player().name +
    constants.MESSAGE_GREET_GET_READY)


def game_loop():
    pc_is_alive = True
    while pc_is_alive and player.Player.points < constants.POINTS_WIN:
        animal_encountered = animal_utils.get_random_animal()
        print(animal_encountered.name, constants.MESSAGE_ENCOUNTER_ANIMAL_NAME)

        animal_attack = get_animal_attack(animal_encountered)
        pc_action = get_pc_action()
        pc_survived_encounter = pc_survives_encounter(animal_attack, pc_action)

        if not pc_survived_encounter:
            pc_is_alive = False
            game_end(constants.MESSAGE_GAME_OVER)
        else:
            if player.Player.points == constants.POINTS_WIN:
                game_end(constants.MESSAGE_GAME_WON)
            else:
                print(constants.MESSAGE_ANOTHER_ANIMAL_APPROACHES)


def get_animal_attack(animal_encountered):
    attack_animal = animal_encountered.get_attack_random()
    print(constants.MESSAGE_ANIMAL_ATTACK, attack_animal)
    return attack_animal


def get_pc_action():
    action_pc = player_action.get_action(player.Player())
    return action_pc


def pc_survives_encounter(attack_animal, action_pc):
    if dictionary.attack_response[attack_animal] == action_pc:
        pc_survives = True
        player_utils.add_point_pc()
        print(constants.MESSAGE_PLAYER_SURVIVED_TRUE)
    else:
        pc_survives = False
        print(constants.MESSAGE_PLAYER_SURVIVED_FALSE)
    return pc_survives


def game_end(message):
    print(message)
    print(constants.MESSAGE_POINTS_PC, player.Player.points)


def game():
    welcome_pc()
    game_loop()


game()
