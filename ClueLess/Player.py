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

    ROOM_NAMES = [
        ["Study", None, "Hall", None, "Lounge"],
        [None, None, None, None, None],
        ["Library", None, "Billiard", None, "Dining"],
        [None, None, None, None, None],
        ["Conservatory", None, "Ballroom", None, "Kitchen"],
    ]

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

    def getRoom(self):
        row, col = self.location
        return self.ROOM_NAMES[row][col]

    def isInRoom(self):
        """Returns whether the player is in a room (vs. a hallway)"""
        room_locations = [
            (0, 0),
            (2, 0),
            (4, 0),
            (0, 2),
            (2, 2),
            (4, 2),
            (0, 4),
            (2, 4),
            (4, 4),
        ]
        return self.location in room_locations

    def setRoom(self, room):
        for r in range(len(self.ROOM_NAMES)):
            for c in range(len(self.ROOM_NAMES[r])):
                if self.ROOM_NAMES[r][c] == room:
                    self.setLocation((r, c))

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
