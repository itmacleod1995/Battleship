import random
from destroyer import Destroyer
class Computer:
    def __init__(self, board):
        self.board = board
        self.destroyerCoordinates = [[(2,3), (2,4)], [(5,7), (6,7)]]

    def setUpBoard(self, file):
        #set up destroyer
        destroyer = Destroyer("D")
        destroyerCoordinate = random.choice(self.destroyerCoordinates)
        for coordinate in destroyerCoordinate:
            self.board.addShip(coordinate[0], coordinate[1], destroyer)












