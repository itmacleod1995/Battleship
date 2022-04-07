from board import Board
from ship import Ship
from destroyer import Destroyer
from player import Player
from carrier import Carrier

print("----Battleship Game----\n")

def run_game():

    playerBoard = Board()
    player = Player(playerBoard)
    computerBoard = Board()
    computerPlayer = Player(computerBoard)

    playerBoard.setUpBoard(player)
    print(player.shipLocations)

    print("Player's board: ")
    playerBoard.showBoard()
    print("Computer's board: ")
    computerBoard.showBoard()
    print("")

    game = True
    while game:
        print("Player 1's turn: ")
        x = int(input("Enter x coordinate: "))
        y = int(input("Enter y coordinate: "))
        player.fire(x, y, computerBoard)
        break




if __name__ == "__main__":
    run_game()