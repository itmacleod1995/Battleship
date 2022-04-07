import numpy as np
from board import Board
from ship import Ship
from player import Player



print("----Battleship Game----")

def run_game():
    player1Board = Board()
    player1 = Player(player1Board)
    player1Board.addShip(4,3)
    computerBoard = Board()
    computerPlayer = Player(computerBoard)
    computerBoard.addShip(2,1)
    print("Player's board: ")
    player1Board.showBoard()
    print("Computer's board: ")
    computerBoard.showBoard()
    print("")

    game = True
    while game:
        print("Player 1's turn: ")
        x = int(input("Enter x coordinate: "))
        y = int(input("Enter y coordinate: "))
        player1.fire(x, y, computerBoard)
        break




if __name__ == "__main__":
    run_game()