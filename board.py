from ship import Ship
from player import Player
from destroyer import Destroyer
from carrier import Carrier


class Board:
    def __init__(self):
        self.rows = 10
        self.cols = 10
        self.board = [["■" for x in range(self.rows)] for y in range(self.cols)]

    def showBoard(self):
        print("")
        for row in self.board:
            print(row)
        print("")

    def addShip(self, x, y, ship):
        self.board[x][y] = ship.name
        ship.coordinates.append((x,y))









