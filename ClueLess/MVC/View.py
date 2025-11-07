import pygame

from ClueLess.Constants import LOCATION_NAMES
from ClueLess.MVC.GuiComponents import (
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    Box,
    Button,
    Color,
    Font,
    Text,
    TextBox,
)
from ClueLess.States import AppState, GameState, MenuState


class View:
    """
    The View for the Clue-Less application

    The View class serves as the GUI for our Clue-Less application. It acts as
    the View in the Model-View-Controller (MVC) architecture.

    Attributes:
        model (ClueLess.MVC.Model):
            The model to display in this view
        screen (pygame.display.Surface):
            The main display
        components (list):
            The list of GUI components to draw
    """

    def __init__(self, model):
        """
        Initializes a new view

        Parameters:
            model (ClueLess.MVC.Model):
                The model to update this view with
        """
        self.model = model

        # Main screen
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Clue-Less")

        # Components to draw on screen
        self.components = []

    def getComponentById(self, id):
        """
        Gets the component with the given ID

        Parameters:
            id (string):
                The component's ID
        """
        for component in self.components:
            if component.getID() == id:
                return component

    def getClickedComponent(self, point):
        """
        Gets the clicked component of the given point

        Parameters:
            point (tuple):
                The x and y coordinates of a point to find a component at
        """
        for component in self.components:
            if component.getArea().collidepoint(point):
                return component

    def deactivateAllButTargetTextBox(self, target):
        """
        Deactivates all of the text boxes except for the target text box

        Parameters:
            target (ClueLess.MVC.TextBox):
                The text box to activate
        """
        for component in self.components:
            if isinstance(component, TextBox):
                if component == target:
                    component.activate()
                else:
                    component.deactivate()

    def updateActiveTextBox(self, event):
        """
        Updates the active text box

        Parameters:
            event (string):
                The event to use to update the text box
        """
        for component in self.components:
            if isinstance(component, TextBox):
                if component.isActive():
                    component.updateText(event)

    def activateAllButtons(self):
        """Activates all button components"""
        for component in self.components:
            if isinstance(component, Button):
                component.activate()

    def deactivateAllButtons(self):
        """Deactivates all button components"""
        for component in self.components:
            if isinstance(component, Button):
                component.deactivate()

    def prepareMenu(self):
        """
        Prepares the menu view

        It contains functions that handle each menu view
        """

        def prepareMainMenu():
            """Prepares the main menu"""
            # Reset components
            self.components = []

            # Title
            self.components.append(
                Text(
                    id="Title",
                    x=SCREEN_WIDTH // 2,
                    y=150,
                    width=180,
                    height=60,
                    borderThickness=0,
                    borderRadius=12,
                    borderColor=Color.BLACK,
                    inactiveFillColor=Color.BLACK,
                    activeFillColor=Color.BLACK,
                    text="Clue-Less",
                    textColor=Color.BLACK,
                    textHighlight=None,
                    font=Font.DEFAULT,
                    active=False,
                )
            )

            # Quit Button
            self.components.append(
                Button(
                    id="QuitButton",
                    x=80,
                    y=50,
                    width=100,
                    height=40,
                    borderThickness=2,
                    borderRadius=12,
                    borderColor=Color.BLACK,
                    inactiveFillColor=Color.GRAY,
                    activeFillColor=Color.GRAY,
                    text="Quit",
                    textColor=Color.BLACK,
                    textHighlight=None,
                    font=Font.DEFAULT,
                    active=True,
                )
            )

            # Host Button
            self.components.append(
                Button(
                    id="HostButton",
                    x=SCREEN_WIDTH // 3,
                    y=(SCREEN_HEIGHT // 3) * 2,
                    width=180,
                    height=60,
                    borderThickness=2,
                    borderRadius=12,
                    borderColor=Color.BLACK,
                    inactiveFillColor=Color.DARK_GRAY,
                    activeFillColor=Color.GRAY,
                    text="Host",
                    textColor=Color.BLACK,
                    textHighlight=None,
                    font=Font.DEFAULT,
                    active=True,
                )
            )

            # Join Button
            self.components.append(
                Button(
                    id="JoinButton",
                    x=(SCREEN_WIDTH // 3) * 2,
                    y=(SCREEN_HEIGHT // 3) * 2,
                    width=180,
                    height=60,
                    borderThickness=2,
                    borderRadius=12,
                    borderColor=Color.BLACK,
                    inactiveFillColor=Color.GRAY,
                    activeFillColor=Color.GRAY,
                    text="Join",
                    textColor=Color.BLACK,
                    textHighlight=None,
                    font=Font.DEFAULT,
                    active=True,
                )
            )

        def prepareServerMenu():
            """Prepares the server menu"""
            # Reset components
            self.components = []

            # Title
            self.components.append(
                Text(
                    id="Title",
                    x=SCREEN_WIDTH // 2,
                    y=150,
                    width=180,
                    height=60,
                    borderThickness=0,
                    borderRadius=12,
                    borderColor=Color.BLACK,
                    inactiveFillColor=Color.BLACK,
                    activeFillColor=Color.BLACK,
                    text="Server Menu",
                    textColor=Color.BLACK,
                    textHighlight=None,
                    font=Font.DEFAULT,
                    active=False,
                )
            )

            # Back Button
            self.components.append(
                Button(
                    id="BackButton",
                    x=80,
                    y=50,
                    width=100,
                    height=40,
                    borderThickness=2,
                    borderRadius=12,
                    borderColor=Color.BLACK,
                    inactiveFillColor=Color.GRAY,
                    activeFillColor=Color.GRAY,
                    text="Back",
                    textColor=Color.BLACK,
                    textHighlight=None,
                    font=Font.DEFAULT,
                    active=True,
                )
            )

            # IP Address
            self.components.append(
                Text(
                    id="IpAddressText",
                    x=480,
                    y=250,
                    width=180,
                    height=60,
                    borderThickness=0,
                    borderRadius=12,
                    borderColor=Color.BLACK,
                    inactiveFillColor=Color.BLACK,
                    activeFillColor=Color.BLACK,
                    text="IP Address",
                    textColor=Color.BLACK,
                    textHighlight=None,
                    font=Font.DEFAULT,
                    active=False,
                )
            )
            self.components.append(
                TextBox(
                    id="IpAddressTextBox",
                    x=700,
                    y=250,
                    width=300,
                    height=40,
                    borderThickness=2,
                    borderRadius=12,
                    borderColor=Color.BLACK,
                    inactiveFillColor=Color.DARK_GRAY,
                    activeFillColor=Color.GRAY,
                    text="",
                    textColor=Color.BLACK,
                    textHighlight=None,
                    font=Font.DEFAULT,
                    active=False,
                )
            )

            # Port
            self.components.append(
                Text(
                    id="PortText",
                    x=480,
                    y=300,
                    width=180,
                    height=60,
                    borderThickness=0,
                    borderRadius=12,
                    borderColor=Color.BLACK,
                    inactiveFillColor=Color.BLACK,
                    activeFillColor=Color.BLACK,
                    text="Port",
                    textColor=Color.BLACK,
                    textHighlight=None,
                    font=Font.DEFAULT,
                    active=False,
                )
            )
            self.components.append(
                TextBox(
                    id="PortTextBox",
                    x=700,
                    y=300,
                    width=300,
                    height=40,
                    borderThickness=2,
                    borderRadius=12,
                    borderColor=Color.BLACK,
                    inactiveFillColor=Color.DARK_GRAY,
                    activeFillColor=Color.GRAY,
                    text="",
                    textColor=Color.BLACK,
                    textHighlight=None,
                    font=Font.DEFAULT,
                    active=False,
                )
            )

            # Max Players
            self.components.append(
                Text(
                    id="MaxPlayersText",
                    x=480,
                    y=350,
                    width=180,
                    height=60,
                    borderThickness=0,
                    borderRadius=12,
                    borderColor=Color.BLACK,
                    inactiveFillColor=Color.BLACK,
                    activeFillColor=Color.BLACK,
                    text="Max Players",
                    textColor=Color.BLACK,
                    textHighlight=None,
                    font=Font.DEFAULT,
                    active=False,
                )
            )
            self.components.append(
                TextBox(
                    id="MaxPlayersTextBox",
                    x=700,
                    y=350,
                    width=300,
                    height=40,
                    borderThickness=2,
                    borderRadius=12,
                    borderColor=Color.BLACK,
                    inactiveFillColor=Color.DARK_GRAY,
                    activeFillColor=Color.GRAY,
                    text="",
                    textColor=Color.BLACK,
                    textHighlight=None,
                    font=Font.DEFAULT,
                    active=False,
                )
            )

            # Host Button
            self.components.append(
                Button(
                    id="HostButton",
                    x=SCREEN_WIDTH // 2,
                    y=500,
                    width=180,
                    height=60,
                    borderThickness=2,
                    borderRadius=12,
                    borderColor=Color.BLACK,
                    inactiveFillColor=Color.GRAY,
                    activeFillColor=Color.GRAY,
                    text="Host",
                    textColor=Color.BLACK,
                    textHighlight=None,
                    font=Font.DEFAULT,
                    active=True,
                )
            )

        def prepareClientMenu():
            """Prepares the client menu"""
            # Reset components
            self.components = []

            # Title
            self.components.append(
                Text(
                    id="Title",
                    x=SCREEN_WIDTH // 2,
                    y=150,
                    width=180,
                    height=60,
                    borderThickness=0,
                    borderRadius=12,
                    borderColor=Color.BLACK,
                    inactiveFillColor=Color.BLACK,
                    activeFillColor=Color.BLACK,
                    text="Client Menu",
                    textColor=Color.BLACK,
                    textHighlight=None,
                    font=Font.DEFAULT,
                    active=False,
                )
            )

            # Back Button
            self.components.append(
                Button(
                    id="BackButton",
                    x=80,
                    y=50,
                    width=100,
                    height=40,
                    borderThickness=2,
                    borderRadius=12,
                    borderColor=Color.BLACK,
                    inactiveFillColor=Color.GRAY,
                    activeFillColor=Color.GRAY,
                    text="Back",
                    textColor=Color.BLACK,
                    textHighlight=None,
                    font=Font.DEFAULT,
                    active=True,
                )
            )

            # IP Address
            self.components.append(
                Text(
                    id="IpAddressText",
                    x=480,
                    y=250,
                    width=180,
                    height=60,
                    borderThickness=0,
                    borderRadius=12,
                    borderColor=Color.BLACK,
                    inactiveFillColor=Color.BLACK,
                    activeFillColor=Color.BLACK,
                    text="IP Address",
                    textColor=Color.BLACK,
                    textHighlight=None,
                    font=Font.DEFAULT,
                    active=False,
                )
            )
            self.components.append(
                TextBox(
                    id="IpAddressTextBox",
                    x=700,
                    y=250,
                    width=300,
                    height=40,
                    borderThickness=2,
                    borderRadius=12,
                    borderColor=Color.BLACK,
                    inactiveFillColor=Color.DARK_GRAY,
                    activeFillColor=Color.GRAY,
                    text="",
                    textColor=Color.BLACK,
                    textHighlight=None,
                    font=Font.DEFAULT,
                    active=False,
                )
            )

            # Port
            self.components.append(
                Text(
                    id="PortText",
                    x=480,
                    y=300,
                    width=180,
                    height=60,
                    borderThickness=0,
                    borderRadius=12,
                    borderColor=Color.BLACK,
                    inactiveFillColor=Color.BLACK,
                    activeFillColor=Color.BLACK,
                    text="Port",
                    textColor=Color.BLACK,
                    textHighlight=None,
                    font=Font.DEFAULT,
                    active=False,
                )
            )
            self.components.append(
                TextBox(
                    id="PortTextBox",
                    x=700,
                    y=300,
                    width=300,
                    height=40,
                    borderThickness=2,
                    borderRadius=12,
                    borderColor=Color.BLACK,
                    inactiveFillColor=Color.DARK_GRAY,
                    activeFillColor=Color.GRAY,
                    text="",
                    textColor=Color.BLACK,
                    textHighlight=None,
                    font=Font.DEFAULT,
                    active=False,
                )
            )

            # Join Button
            self.components.append(
                Button(
                    id="JoinButton",
                    x=SCREEN_WIDTH // 2,
                    y=500,
                    width=180,
                    height=60,
                    borderThickness=2,
                    borderRadius=12,
                    borderColor=Color.BLACK,
                    inactiveFillColor=Color.GRAY,
                    activeFillColor=Color.GRAY,
                    text="Join",
                    textColor=Color.BLACK,
                    textHighlight=None,
                    font=Font.DEFAULT,
                    active=True,
                )
            )

        if self.model.menuState == MenuState.MAIN_MENU:
            # Main Menu
            prepareMainMenu()
        elif self.model.menuState == MenuState.SERVER_MENU:
            # Server Menu
            prepareServerMenu()
        elif self.model.menuState == MenuState.CLIENT_MENU:
            # Client Menu
            prepareClientMenu()

    def prepareGame(self):
        """
        Prepares the game view

        It contains functions that handle each game view
        """

        def prepareGameMenu():
            """Prepares the game menu"""
            # Reset components
            self.components = []

            # Title
            self.components.append(
                Text(
                    id="Title",
                    x=SCREEN_WIDTH // 2,
                    y=150,
                    width=180,
                    height=60,
                    borderThickness=0,
                    borderRadius=12,
                    borderColor=Color.BLACK,
                    inactiveFillColor=Color.BLACK,
                    activeFillColor=Color.BLACK,
                    text="Game Menu",
                    textColor=Color.BLACK,
                    textHighlight=None,
                    font=Font.DEFAULT,
                    active=False,
                )
            )

            # Back Button
            self.components.append(
                Button(
                    id="BackButton",
                    x=80,
                    y=50,
                    width=100,
                    height=40,
                    borderThickness=2,
                    borderRadius=12,
                    borderColor=Color.BLACK,
                    inactiveFillColor=Color.GRAY,
                    activeFillColor=Color.GRAY,
                    text="Back",
                    textColor=Color.BLACK,
                    textHighlight=None,
                    font=Font.DEFAULT,
                    active=True,
                )
            )

            # Display all players
            players = self.model.getPlayers()
            for playerIndex in range(len(players)):
                player = players[playerIndex]
                self.components.append(
                    Text(
                        id=player.getName() + "Text",
                        x=(SCREEN_WIDTH // (len(players) // 2 + 1))
                        * (playerIndex % (len(players) // 2) + 1),
                        y=250 + (playerIndex // (len(players) // 2)) * 100,
                        width=180,
                        height=60,
                        borderThickness=0,
                        borderRadius=12,
                        borderColor=Color.BLACK,
                        inactiveFillColor=Color.BLACK,
                        activeFillColor=Color.BLACK,
                        text=player.getName()
                        + ": "
                        + str(player.getPlayerId())
                        + " "
                        + (
                            "(ME)"
                            if self.model.getPlayerId() == player.getPlayerId()
                            else ""
                        ),
                        textColor=Color.BLACK,
                        textHighlight=None,
                        font=Font.DEFAULT,
                        active=False,
                    )
                )

            if self.model.isServer:
                # Start Button
                self.components.append(
                    Button(
                        id="StartButton",
                        x=SCREEN_WIDTH // 2,
                        y=500,
                        width=180,
                        height=60,
                        borderThickness=2,
                        borderRadius=12,
                        borderColor=Color.BLACK,
                        inactiveFillColor=Color.GRAY,
                        activeFillColor=Color.GRAY,
                        text="Start",
                        textColor=Color.BLACK,
                        textHighlight=None,
                        font=Font.DEFAULT,
                        active=True,
                    )
                )

        def prepareGameplay():
            """Prepares the gameplay"""

            def prepareGameBoard():
                """Prepares the game board"""
                # Current game tilemap
                tilemap = self.model.getTilemap()

                # Board characteristics
                startX = 125
                startY = 220
                roomSize = 150
                roomSpacing = 50

                # Player characteristics
                playerSize = 20

                # 5x5 game board (3x3 rooms + hallways connecting rooms)
                for row in range(5):
                    for column in range(5):
                        # Get the current location name
                        location = LOCATION_NAMES[row][column]
                        if location is None:
                            continue

                        # Get the X and Y location for it
                        currentX = startX + (((roomSize + roomSpacing) // 2) * column)
                        currentY = startY + (((roomSize + roomSpacing) // 2) * row)

                        if row % 2 == 0 and column % 2 == 0:
                            # Room
                            self.components.append(
                                Box(
                                    id=location + "Room",
                                    x=currentX,
                                    y=currentY,
                                    width=roomSize,
                                    height=roomSize,
                                    borderThickness=2,
                                    borderRadius=2,
                                    borderColor=Color.BLACK,
                                    inactiveFillColor=Color.BROWN,
                                    activeFillColor=Color.BROWN,
                                    text=location,
                                    textColor=Color.BLACK,
                                    textHighlight=None,
                                    font=Font.DEFAULT,
                                    active=True,
                                )
                            )

                        elif row % 2 == 0 and column % 2 == 1:
                            # Horizontal Hallway
                            self.components.append(
                                Box(
                                    id=location + "Hallway",
                                    x=currentX,
                                    y=currentY,
                                    width=roomSpacing + 4,
                                    height=roomSpacing,
                                    borderThickness=2,
                                    borderRadius=2,
                                    borderColor=Color.BLACK,
                                    inactiveFillColor=Color.LIGHT_BROWN,
                                    activeFillColor=Color.LIGHT_BROWN,
                                    text="",
                                    textColor=Color.BLACK,
                                    textHighlight=None,
                                    font=Font.DEFAULT,
                                    active=True,
                                )
                            )

                        elif row % 2 == 1 and column % 2 == 0:
                            # Vertical Hallway
                            self.components.append(
                                Box(
                                    id=location + "Hallway",
                                    x=currentX,
                                    y=currentY,
                                    width=roomSpacing,
                                    height=roomSpacing + 4,
                                    borderThickness=2,
                                    borderRadius=2,
                                    borderColor=Color.BLACK,
                                    inactiveFillColor=Color.LIGHT_BROWN,
                                    activeFillColor=Color.LIGHT_BROWN,
                                    text="",
                                    textColor=Color.BLACK,
                                    textHighlight=None,
                                    font=Font.DEFAULT,
                                    active=True,
                                )
                            )

                        # Players for the current location
                        for playerIndex in range(len(tilemap[row][column])):
                            player = tilemap[row][column][playerIndex]

                            # X and Y for the current location in the tilemap
                            x = currentX
                            y = currentY

                            # Adjust x and y for rooms to accommodate multiple players
                            if row % 2 == 0 and column % 2 == 0:
                                # Room
                                x = x - (roomSize // 4) * 1
                                y = y - (roomSize // 4) * 1

                            self.components.append(
                                Box(
                                    id=player.getName() + "Player",
                                    x=x + (roomSize // 4) * (playerIndex % 3),
                                    y=y + (roomSize // 4) * (playerIndex // 3) * 2,
                                    width=playerSize,
                                    height=playerSize,
                                    borderThickness=2,
                                    borderRadius=2,
                                    borderColor=Color.BLACK,
                                    inactiveFillColor=player.getColor(),
                                    activeFillColor=player.getColor(),
                                    text="",
                                    textColor=Color.BLACK,
                                    textHighlight=None,
                                    font=Font.DEFAULT,
                                    active=True,
                                )
                            )

            def prepareTurnDisplay():
                """Prepares the turn display"""
                # Counts
                self.components.append(
                    Text(
                        id="Counts",
                        x=(SCREEN_WIDTH // 4) * 3,
                        y=(SCREEN_HEIGHT // 4),
                        width=180,
                        height=60,
                        borderThickness=0,
                        borderRadius=12,
                        borderColor=Color.BLACK,
                        inactiveFillColor=Color.BLACK,
                        activeFillColor=Color.BLACK,
                        text=f"Red: {self.model.game.red} Green: {self.model.game.green}",
                        # text=f"{vars(self.model.game)}",
                        textColor=Color.BLACK,
                        textHighlight=None,
                        font=Font.DEFAULT,
                        active=False,
                    )
                )

                # Red Button
                self.components.append(
                    Button(
                        id="RedButton",
                        x=(SCREEN_WIDTH // 4) * 3,
                        y=(SCREEN_HEIGHT // 4) * 2,
                        width=180,
                        height=60,
                        borderThickness=2,
                        borderRadius=12,
                        borderColor=Color.BLACK,
                        inactiveFillColor=Color.DARK_GRAY,
                        activeFillColor=Color.RED,
                        text="Red",
                        textColor=Color.BLACK,
                        textHighlight=None,
                        font=Font.DEFAULT,
                        active=True,
                    )
                )

                # Green Button
                self.components.append(
                    Button(
                        id="GreenButton",
                        x=(SCREEN_WIDTH // 4) * 3,
                        y=(SCREEN_HEIGHT // 4) * 3,
                        width=180,
                        height=60,
                        borderThickness=2,
                        borderRadius=12,
                        borderColor=Color.BLACK,
                        inactiveFillColor=Color.DARK_GRAY,
                        activeFillColor=Color.GREEN,
                        text="Green",
                        textColor=Color.BLACK,
                        textHighlight=None,
                        font=Font.DEFAULT,
                        active=True,
                    )
                )

                #########################
                # ADD TURN BUTTONS HERE #
                #########################
                pass

            # Reset components
            self.components = []

            # Title
            self.components.append(
                Text(
                    id="Title",
                    x=SCREEN_WIDTH // 2,
                    y=100,
                    width=180,
                    height=60,
                    borderThickness=0,
                    borderRadius=12,
                    borderColor=Color.BLACK,
                    inactiveFillColor=Color.BLACK,
                    activeFillColor=Color.BLACK,
                    text="Gameplay",
                    textColor=Color.BLACK,
                    textHighlight=None,
                    font=Font.DEFAULT,
                    active=False,
                )
            )

            # Back Button
            self.components.append(
                Button(
                    id="BackButton",
                    x=80,
                    y=50,
                    width=100,
                    height=40,
                    borderThickness=2,
                    borderRadius=12,
                    borderColor=Color.BLACK,
                    inactiveFillColor=Color.GRAY,
                    activeFillColor=Color.GRAY,
                    text="Back",
                    textColor=Color.BLACK,
                    textHighlight=None,
                    font=Font.DEFAULT,
                    active=True,
                )
            )

            # Game Board
            prepareGameBoard()

            # Turn Interaction
            prepareTurnDisplay()

            # Log
            self.components.append(
                Text(
                    id="LogText",
                    x=(SCREEN_WIDTH // 4) * 3,
                    y=(SCREEN_HEIGHT // 10) * 9,
                    width=180,
                    height=60,
                    borderThickness=0,
                    borderRadius=12,
                    borderColor=Color.BLACK,
                    inactiveFillColor=Color.BLACK,
                    activeFillColor=Color.BLACK,
                    text=self.model.getLog(),
                    textColor=Color.BLACK,
                    textHighlight=None,
                    font=Font.DEFAULT,
                    active=False,
                )
            )

        if self.model.gameState == GameState.GAME_MENU:
            # Game Menu
            prepareGameMenu()
        elif self.model.gameState == GameState.GAMEPLAY:
            # Game Play
            prepareGameplay()

    def prepareView(self):
        """Prepares the view"""
        if self.model.appState == AppState.MENU:
            # Menu
            self.prepareMenu()
        elif self.model.appState == AppState.GAME:
            # Game
            self.prepareGame()

    def updateView(self):
        """Updates the view"""
        # Clear display
        self.screen.fill(Color.WHITE)

        for component in self.components:
            # Draw each component
            component.draw(self.screen)

        pygame.display.flip()
