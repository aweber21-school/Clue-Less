import pygame

from ClueLess.Constants import LOCATION_NAMES
from ClueLess.Events import (
    CLIENT_CONNECTED_EVENT,
    CLIENT_COULD_NOT_CONNECT_EVENT,
    CLIENT_DISCONNECTED_EVENT,
    CLIENT_MESSAGE_RECEIVED_EVENT,
    SERVER_CONNECTED_EVENT,
    SERVER_COULD_NOT_START_EVENT,
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
        self.pending_turn = None  # holds the in-progress Turn
        self.room = None

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
                            self.model.isServer = True

                            # Start the client after the server starts up
                            for i in range(10000):
                                # Loop until server is up but don't run
                                # infinitely in case incorrect ip address and
                                # port are used so server startup fails
                                if self.network.server.running:
                                    break
                            self.network.startClient(ipAddress, int(port))

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

                            # Start the client
                            self.network.startClient(ipAddress, int(port))

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

    def _start_pending_turn(self):
        """Create a pending turn if one doesn't exist."""
        if self.pending_turn is None:
            self.pending_turn = Turn()
            self.view.deactivateComponent("ResetButton")

            # If your networking layer needs clientPort on the turn now, attach it:
            if hasattr(self.network, "getClientPort"):
                setattr(self.pending_turn, "clientPort", self.network.getClientPort())

    def _reset_pending_turn(self):
        """Clear pending turn + UI."""
        self.pending_turn = None

        self.view.activateAllButtons()
        self.view.deactivateComponent("SuggestionButton")
        self.view.deactivateComponent("SubmitButton")
        self.view.deactivateComponent("ResetButton")

    def _enable_post_move_ui(self, in_room: bool):
        """Enable the right buttons after movement."""
        self.view.deactivateMovementButtons()
        self.view.activateComponent("ResetButton")
        if in_room:
            self.view.activateComponent("SuggestionButton")
            self.view.deactivateComponent("SubmitButton")
        else:
            self.view.deactivateComponent("SuggestionButton")
            self.view.activateComponent("SubmitButton")

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
                        self.model.isServer = False
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
                        if component.id == "StartButton":
                            # Start button
                            self.model.updateState(
                                appState=AppState.GAME, gameState=GameState.GAMEPLAY
                            )

                            # Start game to signal clients to start
                            self.model.startGame()
                            self.network.sendToClients(self.model.getGame())

                            self.view.prepareView()
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
                                self.model.isServer = False
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

            elif event.type == SERVER_COULD_NOT_START_EVENT:
                # Server could not start
                if self.network.isServer():
                    # The network is a server
                    self.model.updateState(
                        appState=AppState.MENU, menuState=MenuState.SERVER_MENU
                    )

                    # Stop server
                    self.network.stopServer()
                    self.model.isServer = False
                else:
                    # The network is a client
                    self.model.updateState(
                        appState=AppState.MENU, menuState=MenuState.CLIENT_MENU
                    )
                # Stop client
                self.network.stopClient()

                self.model.endGame()
                self.view.prepareView()

            elif event.type == SERVER_CONNECTED_EVENT:
                # Server connected to new client
                if self.network.isServer():
                    # Update players
                    playerIds = event.clientPorts
                    self.model.updatePlayers(playerIds)

                    # Rebroadcast players to sync all clients
                    self.network.sendToClients(self.model.getGame())

            elif event.type == SERVER_MESSAGE_RECEIVED_EVENT:
                # Server received message from client
                pass

            elif event.type == SERVER_DISCONNECTED_EVENT:
                # Server disconnected from client
                if self.network.isServer():
                    # Update players
                    playerIds = event.clientPorts
                    self.model.updatePlayers(playerIds)

                    # Rebroadcast players to sync all clients
                    self.network.sendToClients(self.model.getGame())

            elif event.type == CLIENT_COULD_NOT_CONNECT_EVENT:
                # Client could not connect to server
                self.model.updateState(
                    appState=AppState.MENU,
                    menuState=MenuState.CLIENT_MENU,
                )
                self.network.stopClient()

                self.model.endGame()
                self.view.prepareView()

            elif event.type == CLIENT_CONNECTED_EVENT:
                # Client connected to server
                pass

            elif event.type == CLIENT_MESSAGE_RECEIVED_EVENT:
                # Client received message from server
                server = event.sender
                game = event.message

                if game.running:
                    # Game running attribute signals clients to run
                    self.model.updateState(
                        appState=AppState.GAME, gameState=GameState.GAMEPLAY
                    )

                # Extract client port to save for player ID
                self.model.updatePlayerId(game.__dict__.pop("clientPort"))

                self.model.updateGame(game)
                self.view.prepareView()

                if not self.model.isServer:
                    self.view.deactivateAllButtons()

                # Activate or deactivate inputs as needed
                if self.model.isMyTurn():
                    self.view.activateAllButtons()
                    self.view.deactivateComponent("ResetButton")
                else:
                    self.view.deactivateAllButtons()

            elif event.type == CLIENT_DISCONNECTED_EVENT:
                # Client disconnected from server
                self.model.updateState(
                    appState=AppState.MENU,
                    menuState=MenuState.CLIENT_MENU,
                )
                self.network.stopClient()

                self.model.endGame()
                self.view.prepareView()

            return True

        def handleGameplayInput():
            """Handles the game input"""
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
                        if component.id == "BackButton":
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

                        #################################
                        # ADD TURN BUTTON HANDLING HERE #
                        #################################
                        else:
                            # Build up a single pending turn across multiple clicks
                            self._start_pending_turn()

                            if component.id in [
                                "UpButton",
                                "DownButton",
                                "RightButton",
                                "LeftButton",
                                "StayButton",
                                "NWShortcut",
                                "NEShortcut",
                                "SEShortcut",
                                "SWShortcut",
                            ]:
                                # Movement buttons
                                if component.isActive():
                                    setattr(
                                        self.pending_turn, "move", component.direction
                                    )
                                    # Get new position and determine if player is in a room
                                    row, col = (
                                        self.model.getGame()
                                        .getCurrentPlayer()
                                        .getLocation()
                                    )
                                    if component.direction == "UP":
                                        row -= 1
                                    elif component.direction == "DOWN":
                                        row += 1
                                    elif component.direction == "LEFT":
                                        col -= 1
                                    elif component.direction == "RIGHT":
                                        col += 1
                                    elif component.direction == "NW":
                                        row, col = 0, 0
                                    elif component.direction == "NE":
                                        row, col = 0, 4
                                    elif component.direction == "SE":
                                        row, col = 4, 4
                                    elif component.direction == "SW":
                                        row, col = 4, 0

                                    in_room = col % 2 == 0 and row % 2 == 0
                                    # Disable movement after one move has been done
                                    self.view.deactivateMovementButtons()

                                    # Enable suggestion if in a room
                                    if in_room:
                                        self.room = LOCATION_NAMES[row][col]
                                        self.view.activateComponent("SuggestionButton")
                                    else:
                                        # Otherwise enable submit
                                        self.view.activateComponent("SubmitButton")

                                    self._enable_post_move_ui(in_room)

                            # Accusationi (Any point during turn, but only once)
                            elif component.id == "AccusationButton":
                                if component.isActive():
                                    accusation = self.view.openAccusationMenu()
                                    if accusation is not None:
                                        setattr(
                                            self.pending_turn, "accusation", accusation
                                        )

                                        # After accusation, allow submit, but disable everything else
                                        self.view.deactivateComponent(
                                            "AccusationButton"
                                        )
                                        self.view.deactivateComponent(
                                            "SuggestionButton"
                                        )
                                        self.view.deactivateMovementButtons()
                                        self.view.activateComponent("SubmitButton")

                            # Suggestion (only after movement and only once)
                            elif component.id == "SuggestionButton":
                                if component.isActive():
                                    suggestion = self.view.openSuggestionMenu(self.room)
                                    if suggestion is not None:
                                        setattr(
                                            self.pending_turn, "suggestion", suggestion
                                        )

                                        # After suggestion, allow submit
                                        self.view.deactivateComponent(
                                            "SuggestionButton"
                                        )
                                        self.view.activateComponent("SubmitButton")

                            # Submit (requires movement, and suggestion if we ended in a room)
                            elif component.id == "SubmitButton":
                                if component.isActive():
                                    # Send the fully built turn to the server
                                    self.network.sendToServer(self.pending_turn)

                                    # Lock UI for non-servers if that's your pattern
                                    if not self.model.isServer:
                                        self.view.deactivateAllButtons()

                                    # Clear local state for next turn
                                    self._reset_pending_turn()

                            # Reset
                            elif component.id == "ResetButton":
                                if component.isActive():
                                    # Clear local state
                                    self._reset_pending_turn()

                elif event.button == 2:
                    # Right mouse button clicked
                    pass

                else:
                    # Any other mouse button clicked
                    pass

            elif event.type == SERVER_CONNECTED_EVENT:
                # Server connected to new client
                if self.network.isServer():
                    # Update players
                    playerIds = event.clientPorts
                    self.model.updatePlayers(playerIds)

                    # Rebroadcast game to sync all clients
                    self.network.sendToClients(self.model.getGame())

            elif event.type == SERVER_MESSAGE_RECEIVED_EVENT:
                # Server received message from client
                if self.network.isServer():
                    playerIds = event.clientPorts
                    turn = event.message

                    # Rename clientPort to playerId for better understanding in
                    # Game class
                    turn.playerId = getattr(turn, "clientPort")
                    delattr(turn, "clientPort")

                    # Update players and make the move
                    self.model.updatePlayers(playerIds)
                    self.model.makeMove(turn)

                    # Broadcast to clients
                    self.network.sendToClients(self.model.getGame())

                    # Clear feedback for next move
                    self.model.clearFeedback()

            elif event.type == SERVER_DISCONNECTED_EVENT:
                # Server disconnected from client
                if self.network.isServer():
                    # Update players
                    playerIds = event.clientPorts
                    self.model.updatePlayers(playerIds)

                    # Stop game temporarily
                    self.model.stopGame()

                    # Rebroadcast game to sync all clients
                    self.network.sendToClients(self.model.getGame())

            elif event.type == CLIENT_CONNECTED_EVENT:
                # Client connected to server
                pass

            elif event.type == CLIENT_MESSAGE_RECEIVED_EVENT:
                # Client received message from server
                server = event.sender
                game = event.message

                if not game.running:
                    # Game running attribute signals clients to stop running
                    self.model.updateState(
                        appState=AppState.GAME, gameState=GameState.GAME_MENU
                    )

                # Extract client port to save for player ID
                self.model.updatePlayerId(getattr(game, "clientPort"))
                delattr(game, "clientPort")

                self.model.updateGame(game)
                self.view.prepareView()

                # Activate or deactivate inputs as needed
                if self.model.isMyTurn():
                    self.view.activateAllButtons()
                    self.view.deactivateComponent("ResetButton")
                else:
                    self.view.deactivateAllButtons()

            elif event.type == CLIENT_DISCONNECTED_EVENT:
                # Client disconnected from server
                self.model.updateState(
                    appState=AppState.MENU,
                    menuState=MenuState.CLIENT_MENU,
                )
                self.network.stopClient()

                self.model.endGame()
                self.view.prepareView()

            return True

        if self.model.gameState == GameState.GAME_MENU:
            # Game Menu
            return handleGameMenuInput()
        elif self.model.gameState == GameState.GAMEPLAY:
            # Gameplay
            return handleGameplayInput()

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
