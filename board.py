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

    def setUpBoard(self, player):
        for i in range(len(player.ships)):
            print("Select the spaces you want for your {}".format(player.ships[i]))
            """Destroyer"""
            if player.ships[i] == "destroyer":
                destroyer = Destroyer("D")
                for j in range(2):
                    x = int(input("Enter x coordinate: "))
                    y = int(input("Enter y coordinate: "))
                    destroyer.coordinates.append([x, y])
                    self.addShip(x, y, destroyer)
                player.shipLocations["destroyer"] = destroyer.coordinates
            elif player.ships[i] == "carrier":
                carrier = Carrier("C")
                for j in range(5):
                    x = int(input("Enter x coordinate: "))
                    y = int(input("Enter y coordinate: "))
                    carrier.coordinates.append([x, y])
                    self.addShip(x, y, carrier)
                player.shipLocations["carrier"] = carrier.coordinates
                break

                """Continue here making the next ship"""







