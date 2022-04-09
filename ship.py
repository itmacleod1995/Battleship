class Ship:
    def __init__(self, name):
        self.name = name
        self.space_hit = 0
        self.coordinates = []
        self.isHidden = True

    def printCoordinates(self):
        for coordinate in self.coordinates:
            print("x: {} y: {}".format(coordinate[0], coordinate[1]))


