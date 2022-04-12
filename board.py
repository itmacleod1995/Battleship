from ship import Ship
from player import Player
from destroyer import Destroyer
from carrier import Carrier


class Board:
    """A class used to represent the game board"""
    def __init__(self):
        self.rows = 10
        self.cols = 10
        self.board = [["■" for x in range(self.rows)] for y in range(self.cols)]
        self.dummyBoard = [["■" for x in range(self.rows)] for y in range(self.cols)]

    def showBoard(self):
        """Method that prints the gameboard"""
        print("")
        for row in self.board:
            print(row)
        print("")

    def showComputerBoard(self):
        """Method that prints the computer's gameboard, with all of the ships visible"""
        print("")
        for row in self.dummyBoard:
            print(row)
        print("")

    def addShip(self, x, y, ship):
        """Method that adds a ship to the gameboard based on x and y coordinates"""
        self.board[x][y] = ship.name
        ship.coordinates.append((x,y))









