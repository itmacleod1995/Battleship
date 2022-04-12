from ship import Ship


class Battleship(Ship):
    """
    A class used to represent a battleship, which inherites from the Ship class

    ...

    name : str
        name of ship as a single captial letter (i.e "B" for battleship)
    spaces: int
        how many spaces on the board the ship takes up

    """

    def __init__(self, name):
        """
        Constructs the battleship object
        :param name: name of ship (i.e B for battleship)
        """
        super().__init__(name)
        self.spaces = 4