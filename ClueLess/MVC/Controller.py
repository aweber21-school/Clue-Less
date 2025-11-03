import pygame

from ClueLess.Events import (
    CLIENT_CONNECTED_EVENT,
    CLIENT_DISCONNECTED_EVENT,
    CLIENT_MESSAGE_RECEIVED_EVENT,
    SERVER_CONNECTED_EVENT,
    SERVER_DISCONNECTED_EVENT,
    SERVER_MESSAGE_RECEIVED_EVENT,
)
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

    def handleMenuInput(self, event):
        """
        Handles the menu input

        It contains functions that handle each menu state.

        Parameters:
            event (pygame.event.Event):
                The Pygame event to handle
        """

        def handleMainMenuInput():
            """Handles the main menu input"""
            if event.type == pygame.KEYDOWN:
                # Key pressed
                if event.key == pygame.K_ESCAPE:
                    # Esc key pressed
                    return False
                else:
                    # Any other key pressed
                    pass

            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Mouse button clicked
                if event.button == 1:
                    # Left mouse button clicked
                    component = self.view.getClickedComponent(event.pos)

                    # Activates text box if one is clicked
                    # Deactivates all if none are clicked
                    self.view.deactivateAllButTargetTextBox(component)

                    if component is not None:
                        # A component was clicked
                        if component.id == "HostButton":
                            # Host button
                            self.model.updateState(
                                appState=AppState.MENU, menuState=MenuState.SERVER_MENU
                            )
                            self.view.prepareView()
                        elif component.id == "JoinButton":
                            # Join button
                            self.model.updateState(
                                appState=AppState.MENU, menuState=MenuState.CLIENT_MENU
                            )
                            self.view.prepareView()
                        elif component.id == "QuitButton":
                            # Quit button
                            return False
                        else:
                            # Any other component was clicked
                            pass

                elif event.button == 2:
                    # Right mouse button clicked
                    pass

                else:
                    # Any other mouse button clicked
                    pass

            return True

        def handleServerMenuInput():
            """Handles the server menu input"""
            if event.type == pygame.KEYDOWN:
                # Key pressed
                if event.key == pygame.K_ESCAPE:
                    # Esc key pressed
                    self.model.updateState(
                        appState=AppState.MENU, menuState=MenuState.MAIN_MENU
                    )
                    self.view.prepareView()
                else:
                    # Any other key pressed
                    self.view.updateActiveTextBox(event)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Mouse button clicked
                if event.button == 1:
                    # Left mouse button clicked
                    component = self.view.getClickedComponent(event.pos)

                    # Activates text box if one is clicked
                    # Deactivates all if none are clicked
                    self.view.deactivateAllButTargetTextBox(component)

                    if component is not None:
                        # A component was clicked
                        if component.id == "HostButton":
                            # Host button
                            # Get the values from the text boxes
                            ipAddress = (
                                self.view.getComponentById("IpAddressTextBox")
                            ).getText() or "localhost"
                            port = (
                                self.view.getComponentById("PortTextBox")
                            ).getText() or "5555"
                            maxPlayers = (
                                self.view.getComponentById("MaxPlayersTextBox")
                            ).getText() or "6"

                            # Start the server
                            self.network.startServer(
                                ipAddress, int(port), int(maxPlayers)
                            )

                            # Start the client
                            self.network.startClient(ipAddress, int(port), "ServerHost")

                            self.model.newGame()
                            self.model.updateState(
                                appState=AppState.GAME, gameState=GameState.GAME_MENU
                            )
                            self.view.prepareView()
                        elif component.id == "BackButton":
                            # Back button
                            self.model.updateState(
                                appState=AppState.MENU, menuState=MenuState.MAIN_MENU
                            )
                            self.view.prepareView()

                elif event.button == 2:
                    # Right mouse button clicked
                    pass

                else:
                    # Any other mouse button clicked
                    pass

            return True

        def handleClientMenuInput():
            """Handles the client menu input"""
            if event.type == pygame.KEYDOWN:
                # Key pressed
                if event.key == pygame.K_ESCAPE:
                    # Esc key pressed
                    self.model.updateState(
                        appState=AppState.MENU, menuState=MenuState.MAIN_MENU
                    )
                    self.view.prepareView()
                else:
                    # Any other key pressed
                    self.view.updateActiveTextBox(event)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Mouse button clicked
                if event.button == 1:
                    # Left mouse button clicked
                    component = self.view.getClickedComponent(event.pos)

                    # Activates text box if one is clicked
                    # Deactivates all if none are clicked
                    self.view.deactivateAllButTargetTextBox(component)

                    if component is not None:
                        # A component was clicked
                        if component.id == "JoinButton":
                            # Join button
                            # Get the values from the text boxes
                            ipAddress = (
                                self.view.getComponentById("IpAddressTextBox")
                            ).getText() or "localhost"
                            port = (
                                self.view.getComponentById("PortTextBox")
                            ).getText() or "5555"
                            username = (
                                self.view.getComponentById("UsernameTextBox")
                            ).getText() or "User"

                            # Start the client
                            self.network.startClient(ipAddress, int(port), username)

                            self.model.newGame()
                            self.model.updateState(
                                appState=AppState.GAME, gameState=GameState.GAME_MENU
                            )
                            self.view.prepareView()
                        elif component.id == "BackButton":
                            # Back button
                            self.model.updateState(
                                appState=AppState.MENU, menuState=MenuState.MAIN_MENU
                            )
                            self.view.prepareView()

                elif event.button == 2:
                    # Right mouse button clicked
                    pass

                else:
                    # Any other mouse button clicked
                    pass

            return True

        if self.model.menuState == MenuState.MAIN_MENU:
            # Main Menu
            return handleMainMenuInput()
        elif self.model.menuState == MenuState.SERVER_MENU:
            # Server Menu
            return handleServerMenuInput()
        elif self.model.menuState == MenuState.CLIENT_MENU:
            # Client Menu
            return handleClientMenuInput()

        return True

    def handleGameInput(self, event):
        """
        Handles the game input

        It contains functions that handle each game state.

        Parameters:
            event (pygame.event.Event):
                The Pygame event to handle
        """

        def handleGameMenuInput():
            """Handles the game menu input"""
            if event.type == pygame.KEYDOWN:
                # Key pressed
                if event.key == pygame.K_ESCAPE:
                    # Esc key pressed
                    if self.network.isServer():
                        # The network is a server
                        self.model.updateState(
                            appState=AppState.MENU, menuState=MenuState.SERVER_MENU
                        )

                        # Stop server
                        self.network.stopServer()
                    else:
                        # The network is a client
                        self.model.updateState(
                            appState=AppState.MENU, menuState=MenuState.CLIENT_MENU
                        )
                    # Stop client
                    self.network.stopClient()

                    self.model.endGame()
                    self.view.prepareView()
                else:
                    # Any other key pressed
                    self.view.updateActiveTextBox(event)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Mouse button clicked
                if event.button == 1:
                    # Left mouse button clicked
                    component = self.view.getClickedComponent(event.pos)

                    # Activates text box if one is clicked
                    # Deactivates all if none are clicked
                    self.view.deactivateAllButTargetTextBox(component)

                    if component is not None:
                        # A component was clicked
                        if component.id == "RedButton":
                            # Red button
                            self.network.sendToServer(Turn(red=1))
                        elif component.id == "GreenButton":
                            # Green button
                            self.network.sendToServer(Turn(green=1))
                        elif component.id == "BackButton":
                            # Back button
                            if self.network.isServer():
                                # The network is a server
                                self.model.updateState(
                                    appState=AppState.MENU,
                                    menuState=MenuState.SERVER_MENU,
                                )

                                # Stop server
                                self.network.stopServer()
                            else:
                                # The network is a client
                                self.model.updateState(
                                    appState=AppState.MENU,
                                    menuState=MenuState.CLIENT_MENU,
                                )
                            # Stop client
                            self.network.stopClient()

                            self.model.endGame()
                            self.view.prepareView()

                elif event.button == 2:
                    # Right mouse button clicked
                    pass

                else:
                    # Any other mouse button clicked
                    pass

            elif event.type == SERVER_CONNECTED_EVENT:
                # Server connected to new client
                if self.network.isServer():
                    # Update turn order
                    clientPorts = event.clientPorts
                    self.model.updateTurnOrder(clientPorts)

                    # Rebroadcast game to sync all clients
                    self.network.sendToClients(self.model.getGame())

            elif event.type == SERVER_MESSAGE_RECEIVED_EVENT:
                # Server received message from client
                if self.network.isServer():
                    clientPorts = event.clientPorts
                    turn = event.message

                    # Update turn order and make the move
                    self.model.updateTurnOrder(clientPorts)
                    self.model.makeMove(turn)

                    # Broadcast to clients
                    self.network.sendToClients(self.model.getGame())
                    # self.view.prepareView()

            elif event.type == SERVER_DISCONNECTED_EVENT:
                # Server disconnected from client
                if self.network.isServer():
                    # Update turn order
                    clientPorts = event.clientPorts
                    self.model.updateTurnOrder(clientPorts)

            elif event.type == CLIENT_CONNECTED_EVENT:
                # Client connected to server
                pass

            elif event.type == CLIENT_MESSAGE_RECEIVED_EVENT:
                # Client received message from server
                server = event.sender
                game = event.message

                # Extract client port to save for turn ID
                self.model.updateTurnId(game.__dict__.pop("clientPort"))

                self.model.updateGame(game)
                self.view.prepareView()

                # Activate or deactivate as needed
                if self.model.isMyTurn():
                    self.view.activateAllButtons()
                else:
                    self.view.deactivateAllButtons()

            elif event.type == CLIENT_DISCONNECTED_EVENT:
                # Client disconnected from server
                pass

            return True

        if self.model.gameState == GameState.GAME_MENU:
            # Game Menu
            return handleGameMenuInput()

        return True

    def handleInput(self):
        """Handles the application input"""
        running = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Quit Pygame
                running = False
            elif self.model.appState == AppState.MENU:
                # Menu
                if not self.handleMenuInput(event):
                    running = False
            elif self.model.appState == AppState.GAME:
                # Game
                if not self.handleGameInput(event):
                    running = False
        return running
