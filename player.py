#from board import Board
from destroyer import Destroyer
from carrier import Carrier
from battleship import Battleship
from submarine import Submarine
from patrol import PatrolBoat

class Player:

    def __init__(self, board):
        self.board = board
        self.numOfShips = 5
        self.shipLocations = {}

        """Ships"""
        self.destroyer = Destroyer("D")
        self.carrier = Carrier("C")
        self.battleship = Battleship("B")
        self.submarine = Submarine("S")
        self.patrol = PatrolBoat("P")

        self.shipsSunk = 0

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
                elif "battleship" in line.split(" ")[1]:
                    battleship = Battleship("B")
                    coordinates = line.split(" ")[2:]
                    for c in coordinates:
                        coordinateX = int(c[1])
                        coordinateY = int(c[3])
                        self.board.addShip(coordinateX, coordinateY, battleship)
                elif "submarine" in line.split(" ")[1]:
                    submarine = Submarine("S")
                    coordinates = line.split(" ")[2:]
                    for c in coordinates:
                        coordinateX = int(c[1])
                        coordinateY = int(c[3])
                        self.board.addShip(coordinateX, coordinateY, submarine)
                elif "patrol" in line.split(" ")[1]:
                    patrol = PatrolBoat("P")
                    coordinates = line.split(" ")[2:]
                    for c in coordinates:
                        coordinateX = int(c[1])
                        coordinateY = int(c[3])
                        self.board.addShip(coordinateX, coordinateY, patrol)

    def fire(self, x, y, computerBoard, computer):
        print("Firing at coordinate ({},{})".format(x, y))
        if computerBoard.board[x][y] != "■" and computerBoard.board[x][y] != " ":
            print("Hit!\n")
            computer.addDamageToShip(computerBoard.board[x][y])
            computerBoard.board[x][y] = "X"
        else:
            print("Miss!\n")
            computerBoard.board[x][y] = " "

    def addDamageToShip(self, letterOfShip):
        if letterOfShip == "C":
            self.carrier.space_hit += 1
            if self.carrier.space_hit == self.carrier.spaces:
                print("The computer sunk your carrier!")
                self.shipsSunk += 1
        elif letterOfShip == "D":
            self.destroyer.space_hit += 1
            if self.destroyer.space_hit == self.destroyer.spaces:
                print("The computer sunk your destroyer!")
                self.shipsSunk += 1
        elif letterOfShip == "S":
            self.submarine.space_hit += 1
            if self.submarine.space_hit == self.submarine.spaces:
                print("The computer sunk your submarine!")
                self.shipsSunk += 1
        elif letterOfShip == "B":
            self.battleship.space_hit += 1
            if self.battleship.space_hit == self.battleship.spaces:
                print("The computer sunk your battleship!")
                self.shipsSunk += 1
        elif letterOfShip == "P":
            self.patrol.space_hit += 1
            if self.patrol.space_hit == self.patrol.spaces:
                print("The computer sunk your patrol boat")
                self.shipsSunk += 1





