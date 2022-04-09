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
    computer.setUpBoard("gameFiles/computerShip.txt")

    print("Player's board: ")
    playerBoard.showBoard()
    print("Computer's board: ")
    computerBoard.showBoard()
    print("")

    game = True
    round = 0
    while game:
        if round % 2 == 0:
            print("Player 1's turn: ")
            x = int(input("Enter x coordinate: "))
            y = int(input("Enter y coordinate: "))
            player.fire(x, y, computerBoard, computer)
            computerBoard.showBoard()
            if computer.shipsSunk == 5:
                print("Player wins!")
                break
        else:
            print("Computer's turn")

        round += 1




if __name__ == "__main__":
    run_game()