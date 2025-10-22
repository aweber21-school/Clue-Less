# from ClueLess.States import AppState, MenuState, GameState
from ClueLess.States import State


class Model:
    """
    The Model for the Clue-Less application

    The Model class serves as the source of truth for our Clue-Less
    application. It acts as the Model in the Model-View-Controller (MVC)
    architecture.
    """

    def __init__(self):
        """Initializes a new Model"""
        self.state = State.MAIN_MENU
        # self.appState = AppState.MENU
        # self.menuState = MenuState.MAIN_MENU
        # self.gameState = GameState.GAME_MENU
        self.redCount = 0
        self.greenCount = 0

    def updateCounts(self, redCount, greenCount):
        self.redCount = redCount
        self.greenCount = greenCount

    def updateState(self, state):
        """
        Updates the game state

        Args:
            state (int, States.State):
                The state to update this Model with
        """
        self.state = state

    def updateModel(self):
        """Updates the game state"""
        # Update turn timer?
        pass
