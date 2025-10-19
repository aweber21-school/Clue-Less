from ClueLessController import ClueLessController
from ClueLessModel import ClueLessModel
from ClueLessView import ClueLessView
from Globals import Role

from Server import Server
from Client import Client


class ClueLess:
    """
    The Clue-Less application

    The ClueLess class serves as the top level class for our Clue-Less
    application. It contains the main Pygame game loop and maintains the
    application's Model-View-Controller (MVC). It also is in charge of
    facilitating the Client-Server architecture

    Attributes:
        model (ClueLessModel):
            The game state of the application
        view (ClueLessView):
            The GUI display of the application
        controller (ClueLessController):
            The user input manager of the application
        ???
        running (boolean):
            A flag representing if the application is running
    """

    def __init__(self):
        """Initializes a new Clue-Less application"""
        self.model = ClueLessModel()
        self.view = ClueLessView()
        self.controller = ClueLessController()
        self.role = Role()
        self.running = False

    def stop(self, msg):
        """
        Stops the Clue-Less application

        Args:
            msg (Anything):
                The message to display about stopping the application
        """
        print('Stopping Clue-Less application...')
        print(msg)
        self.running = False
        self.role.stop()
        self.view.closeView()

    def start(self):
        """Starts the Clue-Less application"""
        print('Starting Clue-Less application...')
        self.running = True
        while self.running:
            # Game Loop
            try:
                self.controller.handleInput(self, self.model, self.view)
                self.model.updateModel()
                self.view.updateView(self, self.model, self.controller)
            except KeyboardInterrupt:
                self.stop('KeyboardInterrupt')
            except Exception as e:
                self.stop(e)


if __name__ == '__main__':
    ClueLess().start()
