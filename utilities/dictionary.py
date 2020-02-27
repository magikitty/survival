import utilities.constants as constants

# Dictionary with animal actions (key) and player response (value) that will surive the encounter
attack_response = {
    constants.ATTACK_1: constants.ACTION_1,
    constants.ATTACK_2: constants.ACTION_2,
    constants.ATTACK_3: constants.ACTION_3,
    constants.ATTACK_4: constants.ACTION_1,
    constants.ATTACK_5: constants.ACTION_5,
    constants.ATTACK_CLAWS_1: constants.ACTION_5,
    constants.ATTACK_CLAWS_2: constants.ACTION_1,
    constants.ATTACK_CLAWS_3: constants.ACTION_5,
    constants.ATTACK_CLAWS_4: constants.ACTION_5,
    constants.ATTACK_FLYING_1: constants.ACTION_4,
    constants.ATTACK_FLYING_2: constants.ACTION_5,
    constants.ATTACK_FLYING_3: constants.ACTION_5,
    constants.ATTACK_FLYING_4: constants.ACTION_2,
    constants.ATTACK_WATER_1: constants.ACTION_4,
    constants.ATTACK_WATER_2: constants.ACTION_2,
    constants.ATTACK_WATER_3: constants.ACTION_1,
    constants.ATTACK_WATER_4: constants.ACTION_4
    }

player_input_action = {
    constants.PC_INPUT_1: constants.ACTION_1,
    constants.PC_INPUT_2: constants.ACTION_2,
    constants.PC_INPUT_3: constants.ACTION_3,
    constants.PC_INPUT_4: constants.ACTION_4,
    constants.PC_INPUT_5: constants.ACTION_5
    }
