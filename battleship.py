from ship import Ship

class Battleship(Ship):
    def __init__(self, name):
        super().__init__(name)
        self.spaces = 4