from board import Board
from ship import Ship
from destroyer import Destroyer
from player import Player
from computer import Computer
from carrier import Carrier

print("----Battleship Game----\n")

def run_game():

    """Set up player and board"""
    playerBoard = Board()
    player = Player(playerBoard)
    player.setUpBoard("gameFiles/playerShip.txt")

    """Set Up computer and board"""
    computerBoard = Board()
    computer = Computer(computerBoard)
    #computerPlayer = Player(computerBoard)



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