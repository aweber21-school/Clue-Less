import pygame

from ClueLess.States import State
from ClueLess.Events import NETWORK_EVENT


class Controller:
    """
    The Controller for the Clue-Less application

    The Controller class serves as the mediator for our Clue-Less Model and
    View. It acts as the Controller in the Model-View-Controller (MVC)
    architecture.
    """

    def __init__(self, model, view, network):
        """
        Initializes a new Controller

        Attributes:
            model (ClueLess.MVC.Model):
                The game state of the application
            view.(ClueLess.MVC.View):
                The GUI display of the application
            network (ClueLess.CSV.Network):
                The manager of networking as a client or server
        """
        self.model = model
        self.view = view
        self.network = network

    def handleMainMenuInput(self, event):
        """
        Handles the Main Menu user input

        Args:
            event (pygame.event.Event):
                The Pygame event to handle
        """
        # Esc Button
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            return False

        # Mouse Button Clicked
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Left Mouse Button Clicked
            if event.button == 1:
                # Host Button
                if self.view.host_btn.collidepoint(event.pos):
                    print('Host Pressed')
                    # app.role = Role('Server', Server('localhost', 5555))
                    # app.role.start()
                    self.network.startServer('localhost', 5555)
                    self.model.updateState(State.SERVER_MENU)

                # Join Button
                elif self.view.join_btn.collidepoint(event.pos):
                    print('Join Pressed')
                    # app.role = Role('Client', Client('User', 'localhost', 5555))
                    # app.role.start()
                    self.network.startClient('User', 'localhost', 5555)
                    self.model.updateState(State.CLIENT_MENU)

        return True

    def handleServerMenuInput(self, event):
        """
        Handles the Server Menu user input

        Args:
            event (pygame.event.Event):
                The Pygame event to handle
        """
        # Esc Button
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            self.network.stop()
            self.model.updateState(State.MAIN_MENU)

        # Mouse Button Clicked
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Left Mouse Button Clicked
            if event.button == 1:
                # Back Button
                if self.view.back_btn.collidepoint(event.pos):
                    print('Back Pressed')
                    # app.role.stop()
                    # app.role = Role()
                    self.network.stop()
                    self.model.updateState(State.MAIN_MENU)

        return True

    def handleClientMenuInput(self, event):
        """
        Handles the Client Menu user input

        Args:
            event (pygame.event.Event):
                The Pygame event to handle
        """
        # Esc Button
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            self.network.stop()
            self.model.updateState(State.MAIN_MENU)

        # Mouse Button Clicked
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Left Mouse Button Clicked
            if event.button == 1:
                if self.view.red_btn.collidepoint(event.pos):
                    print('Red Pressed')
                    self.network.network.send_text(f'User|RED')
                    # app.role.getObj().send_text(f'User|RED')
                elif self.view.green_btn.collidepoint(event.pos):
                    print('Green Pressed')
                    self.network.network.send_text(f'User|GREEN')
                    # app.role.getObj().send_text(f'User|GREEN')
                elif self.view.back_btn.collidepoint(event.pos):
                    print('Back Pressed')
                    # app.role.stop()
                    # app.role = Role()
                    self.network.stop()
                    self.model.updateState(State.MAIN_MENU)

        elif event.type == NETWORK_EVENT:
            sender, text = event.payload
            # Example text: "RED:5|GREEN:3"
            if text.startswith('RED:'):
                parts = text.split('|')
                red = int(parts[0].split(':')[1])
                green = int(parts[1].split(':')[1])
                self.model.updateCounts(red, green)

        return True

    def handleInput(self):
        """Handles the Clue-Less user input"""
        running = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif self.model.state == State.MAIN_MENU:
                if not self.handleMainMenuInput(event):
                    running = False
            elif self.model.state == State.SERVER_MENU:
                if not self.handleServerMenuInput(event):
                    running = False
            elif self.model.state == State.CLIENT_MENU:
                if not self.handleClientMenuInput(event):
                    running = False
        return running
