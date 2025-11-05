from ClueLess.Game import Game, Turn
from ClueLess.States import AppState, GameState, MenuState


class Model:
    """
    The Model for the Clue-Less application

    The Model class maintains the app state for our Clue-Less application. It
    acts as the Model in the Model-View-Controller (MVC) architecture.

    Attributes:
        appState (ClueLess.AppState):
            The current app state
        menuState (ClueLess.MenuState):
            The current menu state
        gameState (ClueLess.GameState):
            The current game state
        isServer (boolean):
            The flag of whether this model is a server model
        game (ClueLess.Game):
            The current game
        turn (ClueLess.Turn):
            The current turn
    """

    def __init__(self):
        """Initializes a new model"""
        # States
        self.appState = AppState.MENU
        self.menuState = MenuState.MAIN_MENU
        self.gameState = GameState.GAME_MENU

        # Server Flag
        self.isServer = False

        # Game
        self.playerId = None
        self.game = None
        self.turn = None

    def updateState(self, appState=None, menuState=None, gameState=None):
        """
        Updates the state of the model

        Parameters:
            appState (ClueLess.AppState):
                The new app state
            menuState (ClueLess.MenuState):
                The new menu state
            gameState (ClueLess.GameState):
                The new game state
        """
        if appState is not None:
            self.appState = appState
        if menuState is not None:
            self.menuState = menuState
        if gameState is not None:
            self.gameState = gameState

    def newGame(self):
        """Creates a new game"""
        self.game = Game()

    def endGame(self):
        """Ends the game"""
        self.game = None

    def startGame(self):
        """Start the game"""
        self.game.start()

    def stopGame(self):
        """Stop the game"""
        self.game.stop()

    def getGame(self):
        """Gets the game"""
        return self.game

    def getPlayers(self):
        """Gets the players"""
        return self.game.getPlayers()

    def updatePlayers(self, players):
        """
        Updates the game's players

        Parameters:
            players (list):
                The updated list of players
        """
        self.game.updatePlayers(players)

    def getPlayerId(self):
        """Gets the model's player ID"""
        return self.playerId

    def updatePlayerId(self, playerId):
        """
        Updates the model's player ID

        Parameters:
            playerId (list):
                The updated player ID
        """
        self.playerId = playerId

    def isMyTurn(self):
        """Gets whether it's my turn"""
        return self.playerId == self.game.getCurrentPlayerId()

    def newTurn(self):
        """Starts a new turn"""
        self.turn = Turn()

    def endTurn(self):
        """Ends the turn"""
        self.turn = None

    def getTurn(self):
        """Gets the turn"""
        return self.turn

    def makeMove(self, turn):
        """
        Makes a game move

        Parameters:
            turn (ClueLess.Turn):
                The turn used to make a move
        """
        if not self.game or not turn:
            # No move to make
            return
        else:
            self.game.makeMove(turn)

    def updateGame(self, game):
        """
        Updates the game state

        Parameters:
            game (ClueLess.Game):
                The game to update this model's game to
        """
        if not game:
            # Nothing to update
            return

        self.game = game
