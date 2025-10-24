from ClueLess.States import State


class Model:
    """
    The Model for the Clue-Less application

    The Model class maintains the game state for our Clue-Less application. It
    acts as the Model in the Model-View-Controller (MVC) architecture.

    Attributes:
        state (ClueLess.State):
            The current app state
    """

    def __init__(self):
        """Initializes a new model"""
        self.state = State.MAIN_MENU

        # Debugging
        self.redCount = 0
        self.greenCount = 0

    # Debugging
    def updateCounts(self, redCount, greenCount):
        self.redCount = redCount
        self.greenCount = greenCount

    def updateState(self, state):
        """
        Updates the current app state

        Parameters:
            state (States.State):
                The state to update this model with
        """
        self.state = state

    def updateModel(self):
        """Updates the game state"""
        # Update turn timer?
        pass
