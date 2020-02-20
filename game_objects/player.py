# Class for the player game object
class Player(object):
    def __init__(self, name):
        self.name = name
    def action_player(self):
        action_player = ["roll", "hide"]
    def set_action_player(self):
        action = input("Press 1 or 2: ")
        if action == "1":
            print("You roll")
        if action == "2":
            print("You hide")
        return action


test_player = Player("Sally")
test_player.set_action_player()
