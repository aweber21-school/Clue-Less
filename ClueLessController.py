import pygame

from Globals import State, Role

from Server import Server
from Client import Client, NETWORK_EVENT


class ClueLessController:
    """
    The Controller for the Clue-Less application

    The ClueLessController class serves as the mediator for our Clue-Less
    Model and View. It acts as the Controller in the Model-View-Controller (MVC)
    architecture.
    """

    def __init__(self):
        """Initializes a new Clue-Less Controller"""
        self.red_count = 0
        self.green_count = 0

    def handleMainMenuInput(self, event, app, model, view):
        """
        Handles the Main Menu user input

        Args:
            event (pygame.event.Event):
                The Pygame event to handle
            app (ClueLess):
                The application that facilitates the Client-Server architecture
            model (ClueLessModel):
                The game state to update
            view (ClueLessView):
                The GUI display of the application
        """
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if view.host_btn.collidepoint(event.pos):
                print('Host Pressed')
                app.role = Role('Server', Server('localhost', 5555))
                app.role.start()
                model.updateState(State.SERVER_MENU)
            elif view.join_btn.collidepoint(event.pos):
                print('Join Pressed')
                app.role = Role('Client', Client('User', 'localhost', 5555))
                app.role.start()
                model.updateState(State.CLIENT_MENU)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            app.stop("Ended Gracefully")

    def handleServerMenuInput(self, event, app, model, view):
        """
        Handles the Server Menu user input

        Args:
            event (pygame.event.Event):
                The Pygame event to handle
            app (ClueLess):
                The application that facilitates the Client-Server architecture
            model (ClueLessModel):
                The game state to update
            view (ClueLessView):
                The GUI display of the application
        """
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if view.back_btn.collidepoint(event.pos):
                print('Back Pressed')
                app.role.stop()
                app.role = Role()
                model.updateState(State.MAIN_MENU)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            app.role.stop()
            app.role = Role()
            model.updateState(State.MAIN_MENU)

    def handleClientMenuInput(self, event, app, model, view):
        """
        Handles the Client Menu user input

        Args:
            event (pygame.event.Event):
                The Pygame event to handle
            app (ClueLess):
                The application that facilitates the Client-Server architecture
            model (ClueLessModel):
                The game state to update
            view (ClueLessView):
                The GUI display of the application
        """
        if event.type == NETWORK_EVENT and model.state == State.CLIENT_MENU:
            sender, text = event.payload
            # Example text: "RED:5|GREEN:3"
            if text.startswith("RED:"):
                parts = text.split("|")
                self.red_count = int(parts[0].split(":")[1])
                self.green_count = int(parts[1].split(":")[1])
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if view.red_btn.collidepoint(event.pos):
                print('Red Pressed')
                app.role.getObj().send_text(f'User|RED')
            elif view.green_btn.collidepoint(event.pos):
                print('Green Pressed')
                app.role.getObj().send_text(f'User|GREEN')
            elif view.back_btn.collidepoint(event.pos):
                print('Back Pressed')
                app.role.stop()
                app.role = Role()
                model.updateState(State.MAIN_MENU)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            app.role.stop()
            app.role = Role()
            model.updateState(State.MAIN_MENU)

    def handleInput(self, app, model, view):
        """
        Handles the Clue-Less user input

        Args:
            app (ClueLess):
                The application that facilitates the Client-Server architecture
            model (ClueLessModel):
                The game state to update
            view (ClueLessView):
                The GUI display of the application
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                view.closeView()
            elif model.state == State.MAIN_MENU:
                self.handleMainMenuInput(event, app, model, view)
            elif model.state == State.SERVER_MENU:
                self.handleServerMenuInput(event, app, model, view)
            elif model.state == State.CLIENT_MENU:
                self.handleClientMenuInput(event, app, model, view)
