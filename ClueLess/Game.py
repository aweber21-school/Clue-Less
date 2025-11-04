class Game:
    """
    The Clue-Less Game

    The Game class acts as the Clue-Less game.

    Attributes:
        turnOrder (list):
            List of client ports as turn order identifiers
        currentTurnIndex (int):
            Index of the current turn in the turn order
        # Debugging
        red (int):
            Red button counter
        green (int):
            Green button counter
    """

    def __init__(self):
        """Initializes a new Clue-Less game"""
        # Players
        self.players = []
        self.currentPlayerIndex = 0

        # Debugging
        self.red = 0
        self.green = 0

    def getCurrentPlayerId(self):
        """Returns the current player ID"""
        return self.players[self.currentPlayerIndex]

    def updatePlayers(self, players):
        """
        Updates the game's players

        Parameters:
            players (list):
                The updated list of players
        """
        self.players = players

    def makeMove(self, turn):
        """
        Makes a move

        Parameters:
            turn (ClueLess.Turn):
                The turn to use to make the move
        """
        attributes = vars(turn)

        if int(attributes["clientPort"]) == self.players[self.currentPlayerIndex]:
            # The turn came from the correct player

            # Debugging
            if "red" in attributes.keys():
                self.red += attributes["red"]
            if "green" in attributes.keys():
                self.green += attributes["green"]

            self.currentPlayerIndex = (self.currentPlayerIndex + 1) % len(self.players)

        else:
            # The turn came from the wrong player
            pass


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
