from ship import Ship

class Submarine(Ship):
    def __init__(self, name):
        super().__init__(name)
        self.spaces = 3