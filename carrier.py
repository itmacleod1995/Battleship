from ship import Ship

class Carrier(Ship):
    def __init__(self, name):
        super().__init__(name)
        self.spaces = 4

