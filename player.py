from board import Board
class Player:

    def __init__(self, board):
        self.board = board

    def fire(self, x, y, computerBoard):
        print("Firing at coordinate ({}. {})".format(x, y))
        if computerBoard.board[x][y] != "■":
            print("Hit!")
        else:
            print("Miss!")


