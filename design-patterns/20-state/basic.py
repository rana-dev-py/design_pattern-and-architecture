"""State objects change behavior without conditionals."""
class Locked:
    def press(self, player): player.state = Playing; return "playing"
class Playing:
    def press(self, player): player.state = Locked; return "locked"
class Player:
    def __init__(self): self.state = Locked
    def press(self): return self.state().press(self)

player = Player(); print(player.press(), player.press())
