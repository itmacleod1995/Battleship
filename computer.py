import random
from destroyer import Destroyer
from carrier import Carrier
from battleship import Battleship
from submarine import Submarine
from patrol import PatrolBoat

class Computer:
    def __init__(self, board):
        self.board = board
        self.destroyerCoordinates = [[(2,3), (2,4)], [(5,7), (6,7)], [(2,2), (3,2)], [(7,4), (7,5)]]
        self.carrierCoordinates = [[(0,0), (0,1), (0,2), (0,3), (0,4)], [(3,4), (3,5), (3,6), (3,7), (3,8)]]
        self.battleshipCoordinates = [[(7,0), (7,1), (7,2), (7,3)], [(0,9), (1,9), (2,9), (3,9)], [(8,3), (8,4), (8,5), (8,6)]]
        self.submarineCoordinates = [[(2,7), (2,8), (2,9)], [(8,0), (8,1), (8,2)]]
        self.patrolCoordinates = [[(9,0), (9,1)], [(8,7), (8,8)], [(6,7), (6,8)]]

    def placeShip(self, coordinates, ship):
        for coordinate in coordinates:
            self.board.addShip(coordinate[0], coordinate[1], ship)

    def setUpBoard(self, file):
        #set up destroyer
        destroyer = Destroyer("D")
        destroyerCoordinate = random.choice(self.destroyerCoordinates)
        self.placeShip(destroyerCoordinate, destroyer)

        #set up carrier
        carrier = Carrier("C")
        carrierCoordinates = random.choice(self.carrierCoordinates)
        self.placeShip(carrierCoordinates, carrier)

        #set up battleship
        battleship = Battleship("B")
        battleshipCoordinates = random.choice(self.battleshipCoordinates)
        self.placeShip(battleshipCoordinates, battleship)

        #set up submarine
        sub = Submarine("S")
        submarineCoordinates = random.choice(self.submarineCoordinates)
        self.placeShip(submarineCoordinates, sub)

        # set up patrol boat
        patrol = PatrolBoat("P")
        patrolCoordinates = random.choice(self.patrolCoordinates)
        self.placeShip(patrolCoordinates, patrol)















