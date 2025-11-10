import random

from ClueLess.Cards import Cards
from ClueLess.Player import Player


class Game:
    """
    The Clue-Less Game

    The Game class acts as the Clue-Less game.

    Attributes:
        players (list):
            List of players in the game
        currentTurnIndex (integer):
            Index of the current turn's player
        tilemap (list):
            A 2D list representing the game board
        solution (tuple):
            The solution to the game in the form (character, weapon, room)
        log (string):
            A log message to output
        running (boolean):
            A flag to represent whether or not the Game is running
    """

    def __init__(self):
        """Initializes a new Clue-Less game"""
        # Players
        self.players = [
            Player("MissScarlett"),
            Player("ColonelMustard"),
            Player("MrsWhite"),
            Player("MrGreen"),
            Player("MrsPeacock"),
            Player("ProfessorPlum"),
        ]
        self.currentTurnIndex = 0

        # Tilemap
        self.tilemap = [
            [[], [], [], [], []],
            [[], None, [], None, []],
            [[], [], [], [], []],
            [[], None, [], None, []],
            [[], [], [], [], []],
        ]
        self.updateTilemap()

        # The solution or "truth" set of cards
        self.solution = None

        # Feedback to give players who just made a move
        self.feedback = ""

        # Log to update the players of the game state
        self.log = ""

        # Running
        self.running = False

        ############################
        # ADD GAME ATTRIBUTES HERE #
        ############################

    def getPlayers(self):
        """Gets the players"""
        return self.players

    def updatePlayers(self, playerIds):
        """
        Updates the game's players using a list of player IDs

        Parameters:
            playerIds (list):
                The updated list of player IDs
        """
        playerIdIndex = 0
        for player in self.players:
            # If there isn't a full game, set extra players to have no player ID
            if playerIdIndex >= len(playerIds):
                # All players already assigned to a character
                player.setPlayerId(None)

            elif player.playerId != playerIds[playerIdIndex]:
                # Assign all players to characters in order
                player.setPlayerId(playerIds[playerIdIndex])

            playerIdIndex += 1

    def getTilemap(self):
        """Gets the tilemap"""
        return self.tilemap

    def updateTilemap(self):
        """Updates the tilemap based on the players"""
        self.tilemap = [
            [[], [], [], [], []],
            [[], None, [], None, []],
            [[], [], [], [], []],
            [[], None, [], None, []],
            [[], [], [], [], []],
        ]

        # Add each player to the tilemap
        for player in self.players:
            row = player.location[0]
            column = player.location[1]
            self.tilemap[row][column].append(player)

    def getSolution(self):
        """Gets the solution"""
        return self.solution

    def pickSolution(self):
        """Picks the solution of the game"""
        self.solution = (
            random.choice(Cards.CHARACTERS),
            random.choice(Cards.WEAPONS),
            random.choice(Cards.ROOMS),
        )

    def distributeCards(self):
        """Removes truth set, then distributes remaining cards to players"""
        # Combines all of the cards
        allCards = list(Cards.CHARACTERS + Cards.WEAPONS + Cards.ROOMS)

        # Remove the cards that are part of the solution
        allCards = [card for card in allCards if card not in self.solution]

        playerIndex = 0
        while len(allCards) > 0:
            player = self.players[playerIndex]

            # Only distribute to real players
            if player.getPlayerId() is not None:
                # Get a random card
                card = random.choice(allCards)

                # Add the card to the player
                playerCards = player.getCards()
                playerCards.append(card)
                player.setCards(playerCards)

                # Remove card from master list
                allCards.remove(card)

            # Increment player index
            playerIndex = (playerIndex + 1) % len(self.players)

    def getLog(self):
        """Gets the log"""
        return self.log

    def setLog(self, log):
        """
        Sets the game log

        Parameters:
            log (string):
                The log for the game
        """
        self.log = log

    def getFeedback(self):
        """Gets the feedback"""
        return self.feedback

    def setFeedback(self, feedback):
        """
        Sets the game feedback

        Parameters:
            feedback (string):
                The feedback for the game
        """
        self.feedback = feedback

    def findPlayerFromId(self, playerId):
        """
        Finds the player with the given ID

        Parameters:
            playerId (integer)
                The player ID to find
        """
        for player in self.players:
            if player.getPlayerId() == playerId:
                return player

    def getCurrentPlayer(self):
        """Returns the current player ID"""
        return self.players[self.currentTurnIndex]

    def getPreviousPlayer(self):
        """Returns the previous player ID"""
        turnIndex = self.currentTurnIndex
        while True:
            # Decrement turn index
            turnIndex = (turnIndex - 1 + len(self.players)) % len(self.players)

            if self.players[turnIndex].getPlayerId() is not None:
                # Valid player was found
                break

        return self.players[turnIndex]

    def nextPlayer(self):
        """Sets the current player ID to the next valid player"""
        while True:
            # Increment current player index
            self.currentTurnIndex = (self.currentTurnIndex + 1) % len(self.players)

            if self.getCurrentPlayer().getPlayerId() is not None:
                # Valid player was found
                return

    def start(self):
        """Starts the game"""
        self.running = True

        # Randomly choose solution or "truth" cards
        self.pickSolution()

        # Debugging
        # print(self.solution)

        # Distribute cards to players (without truth set)
        self.distributeCards()

    def stop(self):
        """Stops the game"""
        self.running = False

    def makeMove(self, turn):
        """
        Makes a move

        Parameters:
            turn (ClueLess.Turn):
                The turn to use to make the move
        """
        if (
            hasattr(turn, "playerId")
            and int(turn.playerId) == self.getCurrentPlayer().getPlayerId()
        ):
            # The turn came from the correct player

            #######################
            # ADD TURN LOGIC HERE #
            #######################
            if hasattr(turn, "move"):
                # Update player's current position
                # NOTE: Only valid movements should be possible here, so we don't check
                (row, col) = self.getCurrentPlayer().getLocation()
                if getattr(turn, "move") == "UP":
                    self.getCurrentPlayer().setLocation((row - 1, col))
                elif getattr(turn, "move") == "DOWN":
                    self.getCurrentPlayer().setLocation((row + 1, col))
                elif getattr(turn, "move") == "RIGHT":
                    self.getCurrentPlayer().setLocation((row, col + 1))
                elif getattr(turn, "move") == "LEFT":
                    self.getCurrentPlayer().setLocation((row, col - 1))
                # Log that the player made the move
                self.log = (
                    self.findPlayerFromId(turn.playerId).getName()
                    + " successfully made a move"
                )

            if hasattr(turn, "suggestion"):
                (suspect, weapon, room) = getattr(turn, "suggestion")
                for player in self.players:
                    if player.getName() == suspect:
                        player.setRoom(room)

                self.log = (
                    self.findPlayerFromId(turn.playerId).getName()
                    + f" suggests {suspect}, {weapon}, {room}"
                )

                # Suggestion results
                self.feedback = "No other players have any suggestion cards"

                # Loop through all players starting at the next player and
                # excluding the current player to search for suggestion cards
                for player in (
                    self.players[self.currentTurnIndex + 1 :]
                    + self.players[0 : self.currentTurnIndex]
                ):
                    playerCards = player.getCards()

                    # Look for room first so the player knows to move rooms
                    if room in playerCards:
                        # Player has the room card
                        self.feedback = f"{player.getName()} has the {room} card"
                        break

                    elif weapon in playerCards:
                        # Player has the weapon card
                        self.feedback = f"{player.getName()} has the {weapon} card"
                        break

                    elif suspect in playerCards:
                        # Player has the suspect card
                        self.feedback = f"{player.getName()} has the {suspect} card"
                        break

            self.updateTilemap()
            # Move to the next player
            self.nextPlayer()

        else:
            # The turn came from the wrong player
            pass


class Turn:
    """
    A Turn in the Clue-Less Game

    The Turn class acts as a single turn in the Clue-Less game.

    Attributes:
        * Created dynamically but limited to attributes found in '__slots__'
    """

    # Add potential attributes here so that we know what to expect within a Turn object
    __slots__ = ["clientPort", "playerId", "move", "suggestion"]

    def __init__(self, **kwargs):
        """
        Initializes a turn

        Parameters:
            **kwargs (dict):
                A dictionary of keyword arguments to add as attributes
        """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def update(self, **kwargs):
        """
        Updates the turn

        Parameters:
            **kwargs (dict):
                A dictionary of keyword arguments to add as attributes
        """
        for key, value in kwargs.items():
            setattr(self, key, value)
