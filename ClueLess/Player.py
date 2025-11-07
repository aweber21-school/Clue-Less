from ClueLess.Constants import CHARACTER_COLORS, STARTING_LOCATIONS


class Player:
    """
    A Player in the Clue-Less Game

    The Player class acts as a single player in the Clue-Less game.

    Attributes:
        name (string):
            The name of the player
        playerId (integer):
            The player's ID
        color (tuple):
            The player's color
        location (tuple):
            The location of the player in the tilemap represented in (row, column)
        cards (list):
            The list of cards that this player has
    """

    def __init__(self, name):
        """
        Initializes a new Clue-Less player

        Parameters:
            name (string):
                The name of the player
        """
        self.name = name
        self.playerId = None

        self.color = CHARACTER_COLORS[self.name]

        self.location = STARTING_LOCATIONS[self.name]

        self.cards = []

    def getName(self):
        """Gets the player's name"""
        return self.name

    def getPlayerId(self):
        """Gets the player ID"""
        return self.playerId

    def setPlayerId(self, playerId):
        """
        Sets the player ID

        Parameters:
            playerId (integer):
                The new player ID for this player
        """
        self.playerId = playerId

    def getColor(self):
        """Gets the player's color"""
        return self.color

    def setColor(self, color):
        """
        Sets the player's color'

        Parameters:
            color (tuple):
                The new color for this player
        """
        self.color = color

    def getLocation(self):
        """Gets the player's location"""
        return self.location

    def setLocation(self, location):
        """
        Sets the player's location

        Parameters:
            location (tuple):
                The new location for this player
        """
        self.location = location

    def getCards(self):
        """Gets the player's cards"""
        return self.cards

    def setCards(self, cards):
        """
        Sets the player's cards

        Parameters:
            cards (list):
                The new location for this player
        """
        self.cards = cards
