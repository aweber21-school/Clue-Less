from ClueLessMVC import Model, View, Controller
from ClueLessCSA import Client, Server
from Globals import Role


class ClueLessApp:
    """
    The Clue-Less application

    The ClueLessApp class serves as the top level class for our Clue-Less
    application. It contains the main Pygame game loop and maintains the
    application's Model-View-Controller (MVC). It also is in charge of
    facilitating the Client-Server architecture.

    Attributes:
        model (ClueLessMVC.Model):
            The game state of the application
        view (ClueLessMVC.View):
            The GUI display of the application
        controller (ClueLessMVC.Controller):
            The user input manager of the application
        ???
        running (boolean):
            A flag representing if the application is running
    """

    def __init__(self):
        """Initializes a new Clue-Less app"""
        self.model = Model()
        self.view = View()
        self.controller = Controller()
        self.role = Role()
        self.running = False

    def stop(self, msg):
        """
        Stops the Clue-Less app

        Args:
            msg (Anything):
                The message to display about stopping the application
        """
        print('Stopping Clue-Less app...')
        print(msg)
        self.running = False
        try:
            self.role.stop()
        except AttributeError:
            pass
        self.view.closeView()

    def start(self):
        """Starts the Clue-Less app"""
        print('Starting Clue-Less app...')
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
        self.stop('Ended Gracefully')

if __name__ == '__main__':
    ClueLessApp().start()
