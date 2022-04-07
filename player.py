from board import Board
from destroyer import Destroyer

class Player:

    def __init__(self, board):
        self.board = board
        self.numOfShips = 5
        self.shipLocations = {}
        self.ships = ["destroyer", "carrier", "battleship", "cruiser", "submarine"]

    def fire(self, x, y, computerBoard):
        print("Firing at coordinate ({}. {})".format(x, y))
        if computerBoard.board[x][y] != "■":
            print("Hit!")
        else:
            print("Miss!")


