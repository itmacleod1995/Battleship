import random
from destroyer import Destroyer
from carrier import Carrier
from battleship import Battleship
from submarine import Submarine
from patrol import PatrolBoat

class Computer:
    def __init__(self, board):
        self.board = board
        """Ships"""
        self.destroyer = Destroyer("D")
        self.carrier = Carrier("C")
        self.battleship = Battleship("B")
        self.submarine = Submarine("S")
        self.patrol = PatrolBoat("P")
        """Coordinates"""
        self.destroyerCoordinates = [[(2,3), (2,4)], [(5,7), (6,7)], [(2,2), (3,2)], [(7,4), (7,5)]]
        self.carrierCoordinates = [[(0,0), (0,1), (0,2), (0,3), (0,4)], [(3,4), (3,5), (3,6), (3,7), (3,8)]]
        self.battleshipCoordinates = [[(7,0), (7,1), (7,2), (7,3)], [(0,9), (1,9), (2,9), (3,9)], [(8,3), (8,4), (8,5), (8,6)]]
        self.submarineCoordinates = [[(2,7), (2,8), (2,9)], [(8,0), (8,1), (8,2)]]
        self.patrolCoordinates = [[(9,0), (9,1)], [(8,7), (8,8)], [(6,7), (6,8)]]

        self.shipsSunk = 0

    def fire(self, x, y, player, playerBoard):
        pass



    def placeShip(self, coordinates, ship):
        for coordinate in coordinates:
            self.board.addShip(coordinate[0], coordinate[1], ship)


    def setUpBoard(self, file):
        #set up destroyer
        destroyerCoordinate = random.choice(self.destroyerCoordinates)
        self.placeShip(destroyerCoordinate, self.destroyer)

        #set up carrier
        carrierCoordinates = random.choice(self.carrierCoordinates)
        self.placeShip(carrierCoordinates, self.carrier)

        #set up battleship
        battleshipCoordinates = random.choice(self.battleshipCoordinates)
        self.placeShip(battleshipCoordinates, self.battleship)

        #set up submarine
        submarineCoordinates = random.choice(self.submarineCoordinates)
        self.placeShip(submarineCoordinates, self.submarine)

        # set up patrol boat
        patrolCoordinates = random.choice(self.patrolCoordinates)
        self.placeShip(patrolCoordinates, self.patrol)

    def addDamageToShip(self, letterOfShip):
        if letterOfShip == "D":
            self.destroyer.space_hit += 1
            if self.destroyer.space_hit == self.destroyer.spaces:
                print("The computer's destroyer has been sunk!")
                self.shipsSunk += 1
        elif letterOfShip == "C":
            self.carrier.space_hit += 1
            if self.carrier.space_hit == self.carrier.spaces:
                print("The computer's carrier has been sunk!")
                self.shipsSunk += 1
        elif letterOfShip == "B":
            self.battleship.space_hit += 1
            if self.battleship.space_hit == self.battleship.spaces:
                print("The computer's battleship has been sunk!")
                self.shipsSunk += 1
        elif letterOfShip == "S":
            self.submarine.space_hit += 1
            if self.submarine.space_hit == self.submarine.spaces:
                print("The computer's submarine has been sunk!")
                self.shipsSunk += 1
        elif letterOfShip == "P":
            self.patrol.space_hit += 1
            if self.patrol.space_hit == self.patrol.spaces:
                print("The computer's patrol boat has been sunk!")
                self.shipsSunk += 1


















