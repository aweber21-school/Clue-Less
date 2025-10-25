import pygame

from ClueLess.Events import CLIENT_MESSAGE_RECEIVED_EVENT, SERVER_MESSAGE_RECEIVED_EVENT
from ClueLess.Game import Turn
from ClueLess.States import AppState, GameState, MenuState


class Controller:
    """
    The Controller for the Clue-Less application

    The Controller class serves as the mediator for our Clue-Less Model and
    View. It acts as the Controller in the Model-View-Controller (MVC)
    architecture.

    Attributes:
        model (ClueLess.MVC.Model):
            The game state of the application
        view (ClueLess.MVC.View):
            The GUI display of the application
        network (ClueLess.CSV.Network):
            The manager of networking as a client or server
    """

    def __init__(self, model, view, network):
        """
        Initializes a new controller

        Parameters:
            model (ClueLess.MVC.Model):
                The model of the application
            view (ClueLess.MVC.View):
                The view of the application
            network (ClueLess.CSA.Network):
                The network of the application
        """
        self.model = model
        self.view = view
        self.network = network

    def handleMainMenuInput(self, event):
        """
        Handles the main menu user input

        Parameters:
            event (pygame.event.Event):
                The Pygame event to handle
        """
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            # Esc Button
            return False

        if event.type == pygame.MOUSEBUTTONDOWN:
            # Mouse Button Clicked
            if event.button == 1:
                # Left Mouse Button Clicked
                if self.view.host_btn.collidepoint(event.pos):
                    # Host Button
                    self.network.startServer("localhost", 5555, 6)
                    self.model.newGame()
                    self.model.updateState(menuState=MenuState.SERVER_MENU)

                elif self.view.join_btn.collidepoint(event.pos):
                    # Join Button
                    self.network.startClient("User", "localhost", 5555)
                    self.model.newGame()
                    self.model.updateState(menuState=MenuState.CLIENT_MENU)

        return True

    def handleServerMenuInput(self, event):
        """
        Handles the server menu user input

        Parameters:
            event (pygame.event.Event):
                The Pygame event to handle
        """
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            # Esc Button
            self.network.stopServer()
            self.model.endGame()
            self.model.updateState(menuState=MenuState.MAIN_MENU)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Mouse Button Clicked
            if event.button == 1:
                # Left Mouse Button Clicked
                if self.view.back_btn.collidepoint(event.pos):
                    # Back Button
                    print("Back Pressed")
                    self.network.stopServer()
                    self.model.endGame()
                    self.model.updateState(menuState=MenuState.MAIN_MENU)

        elif event.type == CLIENT_MESSAGE_RECEIVED_EVENT:
            # Server received message from Client
            client = event.sender
            turn = event.message

            self.model.makeMove(turn)
            self.network.sendToClients(self.model.getGame())

        return True

    def handleClientMenuInput(self, event):
        """
        Handles the client menu user input

        Parameters:
            event (pygame.event.Event):
                The Pygame event to handle
        """
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            # Esc Button
            self.network.stopClient()
            self.model.endGame()
            self.model.updateState(menuState=MenuState.MAIN_MENU)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Mouse Button Clicked
            if event.button == 1:
                # Left Mouse Button Clicked
                if self.view.red_btn.collidepoint(event.pos):
                    # Red button
                    self.network.sendToServer(Turn(red=1))
                elif self.view.green_btn.collidepoint(event.pos):
                    # Green button
                    self.network.sendToServer(Turn(green=1))
                elif self.view.back_btn.collidepoint(event.pos):
                    # Back button
                    self.network.stopClient()
                    self.model.endGame()
                    self.model.updateState(menuState=MenuState.MAIN_MENU)

        elif event.type == SERVER_MESSAGE_RECEIVED_EVENT:
            # Client received message from server
            server = event.sender
            game = event.message

            self.model.updateGame(game)

        return True

    def handleInput(self):
        """Handles the application input"""
        running = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif self.model.appState == AppState.MENU:
                # Menu
                if self.model.menuState == MenuState.MAIN_MENU:
                    # Main Menu
                    if not self.handleMainMenuInput(event):
                        running = False
                elif self.model.menuState == MenuState.SERVER_MENU:
                    # Server Menu
                    if not self.handleServerMenuInput(event):
                        running = False
                elif self.model.menuState == MenuState.CLIENT_MENU:
                    # Client Menu
                    if not self.handleClientMenuInput(event):
                        running = False
            elif self.model.appState == AppState.GAME:
                # Game
                if self.model.gameState == GameState.GAME_MENU:
                    pass
        return running
