class Board:
    def __init__(self):
        self.rows = 10
        self.cols = 10
        self.board = [["■" for x in range(self.rows)] for y in range(self.cols)]

    def showBoard(self):
        for row in self.board:
            print(row)
