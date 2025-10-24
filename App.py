from ClueLess.MVC import Model, View, Controller
from ClueLess.CSA import Network


class App:
    """
    The Clue-Less application

    The ClueLessApp class serves as the top level class for our Clue-Less
    application. It contains the main Pygame game loop and maintains the
    application's Model-View-Controller (MVC). It also is in charge of
    facilitating the Client-Server architecture.

    Attributes:
        model (ClueLess.MVC.Model):
            The game state of the application
        view (ClueLess.MVC.View):
            The GUI display of the application
        controller (ClueLess.MVC.Controller):
            The user input manager of the application
        network (ClueLess.CSV.Network):
            The manager of networking as a client or server
    """

    def __init__(self):
        """Initializes a new Clue-Less app"""
        self.model = Model()
        self.view = View(self.model)
        self.network = Network()
        self.controller = Controller(self.model, self.view, self.network)
        self.running = False

    def start(self):
        """Starts the Clue-Less app"""
        print('Starting Clue-Less app...')
        self.running = True
        self.run()

    def stop(self, log=''):
        """
        Stops the Clue-Less app

        Args:
            log (obj):
                The object to display about stopping the application
        """
        print('Stopping Clue-Less app...')
        print(log)
        self.view.closeView()
        self.network.stop()
        self.running = False

    def run(self):
        log = 'Stopped Gracefully'
        while self.running:
            # Game Loop
            try:
                self.running = self.controller.handleInput()
                self.model.updateModel()
                self.view.updateView()
            except KeyboardInterrupt:
                log = 'KeyboardInterrupt'
                self.running = False
            except Exception as e:
                log = str(e)
                self.running = False
        self.stop(log)


if __name__ == '__main__':
    App().start()
