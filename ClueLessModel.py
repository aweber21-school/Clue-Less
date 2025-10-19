from Globals import State


class ClueLessModel:
    """
    The Model for the Clue-Less application

    The ClueLessModel class serves as the source of truth for our Clue-Less
    application. It acts as the Model in the Model-View-Controller (MVC)
    architecture.
    """

    def __init__(self):
        """Initializes a new Clue-Less Model"""
        self.state = State.MAIN_MENU

    def updateState(self, state):
        """
        Updates the game state

        Args:
            state (int, Globals.State):
                The state to update this Model with
        """
        self.state = state

    def updateModel(self):
        """Updates the Clue-Less game state"""
        pass
