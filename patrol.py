from ship import Ship

class PatrolBoat(Ship):
    def __init__(self, name):
        super().__init__(name)
        self.spaces = 2