class Game:
    """
    The Clue-Less Game

    The Game class acts as the Clue-Less game.

    Attributes:
        # Debugging
        red (int):
            Red button counter
        green (int):
            Green button counter
    """

    def __init__(self):
        """Initializes a new Clue-Less game"""
        # Debugging
        self.red = 0
        self.green = 0

    def makeMove(self, turn):
        """
        Makes a move

        Parameters:
            turn (ClueLess.Turn):
                The turn to use to make the move
        """
        attributes = vars(turn)

        # Debugging
        if "red" in attributes.keys():
            self.red += attributes["red"]
        if "green" in attributes.keys():
            self.green += attributes["green"]


class Turn:
    """
    A Turn in the Clue-Less Game

    The Turn class acts as a single turn in the Clue-Less game.

    Attributes:
        * Created dynamically but limited to attributes found in '__slots__'
        * Note: '__dict__' is necessary in order to dynamically add attributes
        and still allow pickle to serialize for socket communication
    """

    __slots__ = ["__dict__", "red", "green"]

    def __init__(self, **kwargs):
        """
        Initializes a turn

        Parameters:
            **kwargs (dict):
                A dictionary of keyword arguments to add as attributes
        """
        self.__dict__.update(kwargs)

    def update(self, **kwargs):
        """
        Updates turn

        Parameters:
            **kwargs (dict):
                A dictionary of keyword arguments to add as attributes
        """
        self.__dict__.update(kwargs)
