#from board import Board
from destroyer import Destroyer
from carrier import Carrier

class Player:

    def __init__(self, board):
        self.board = board
        self.numOfShips = 5
        self.shipLocations = {}
        self.ships = ["destroyer", "carrier", "battleship", "cruiser", "submarine"]

    def setUpBoard(self, file):
        with open(file) as file_object:
            for line in file_object.readlines():
                if "destroyer" in line.split(" ")[1]:
                    destroyer = Destroyer("D")
                    coordinates = line.split(" ")[2:]
                    for c in coordinates:
                        coordinateX = int(c[1])
                        coordinateY = int(c[3])
                        self.board.addShip(coordinateX, coordinateY, destroyer)
                elif "carrier" in line.split(" ")[1]:
                    carrier = Carrier("C")
                    coordinates = line.split(" ")[2:]
                    for c in coordinates:
                        coordinateX = int(c[1])
                        coordinateY = int(c[3])
                        self.board.addShip(coordinateX, coordinateY, carrier)



    def fire(self, x, y, computerBoard):
        print("Firing at coordinate ({}. {})".format(x, y))
        if computerBoard.board[x][y] != "■":
            print("Hit!")
        else:
            print("Miss!")


