# Class for the player game object
class Player(object):
    def __init__(self, name):
        self.name = name
        self.actions = ["roll", "hide"]
    def action(self):
        return set_action_player(self)


def set_action_player(Player):
    action = input("Press 1 or 2: ")
    if action == "1":
        print("You roll")
        return Player.actions[0]
    if action == "2":
        print("You hide")
        return Player.actions[1]
