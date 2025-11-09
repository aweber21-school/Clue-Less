import pygame

from ClueLess.Constants import LOCATION_NAMES
from ClueLess.MVC.GuiComponents import (
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    MovementButton,
    Box,
    Button,
    Color,
    Font,
    SuggestionMenu,
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
        """Activates all button components, but only available movement buttons."""
        for component in self.components:
            if isinstance(component, Button):
                if isinstance(component, MovementButton):
                    # Determine which movement options are available to this player
                    availableDirections = self.determineAvailableDirections()
                    if component.direction not in availableDirections:
                        component.deactivate()
                        continue
                if component.id in ["SuggestionButton", "SubmitButton"]:
                    continue
                component.activate()

    def activateComponent(self, component_id):
        """Activates a component with a specific component_id. 
        If no matching component is found, does nothing"""
        for component in self.components:
            if component.id == component_id:
                component.activate()

    def deactivateComponent(self, component_id):
        """Deactivates a component with a specific component_id. 
        If no matching component is found, does nothing"""
        for component in self.components:
            if component.id == component_id:
                component.deactivate()

    def deactivateAllButtons(self):
        """Deactivates all button components"""
        for component in self.components:
            if isinstance(component, Button):
                component.deactivate()

    def deactivateMovementButtons(self):
        """Deactivates the buttons responsible for movement"""
        for component in self.components:
             if isinstance(component, MovementButton):
                component.deactivate()

    def determineAvailableDirections(self):
        """Determines which movements are available to a player on their turn"""
        # Get current tilemap
        tilemap = self.model.getGame().getTilemap()
        # Get current player's location
        current_player = self.model.getGame().getCurrentPlayer()
        playerRow, playerCol = current_player.getLocation()
        available = {"UP", "DOWN", "RIGHT", "LEFT", "STAY"}
        
        # Determine if Stay is avaiable
        if not current_player.isInRoom():
            available.remove("STAY")

        # Determine if Up is available
        if playerRow == 0:
            # Top Row
            available.remove("UP")
        elif tilemap[playerRow - 1][playerCol] is None:
            # Hallway below an empty space
            available.remove("UP")
        elif current_player.isInRoom() and len(tilemap[playerRow - 1][playerCol]) != 0:
            # Hallway above is blocked
            available.remove("UP")
        
        # Determine if Down is available
        if playerRow == 4:
            # Bottom Row
            available.remove("DOWN")
        elif tilemap[playerRow + 1][playerCol] is None:
            # Hallway above an empty space
            available.remove("DOWN")
        elif current_player.isInRoom() and len(tilemap[playerRow + 1][playerCol]) != 0:
            # Hallway below is blocked
            available.remove("DOWN")

        # Determine if Right is available
        if playerCol == 4:
            # Rightmost Column
            available.remove("RIGHT")
        elif tilemap[playerRow][playerCol + 1] is None:
            # Hallway to the left of an empty space
            available.remove("RIGHT")
        elif current_player.isInRoom() and len(tilemap[playerRow][playerCol + 1]) != 0:
            # Hallway to the right is blocked
            available.remove("RIGHT")

        # Determine if Left is available
        if playerCol == 0:
            # Leftmost Column
            available.remove("LEFT")
        elif tilemap[playerRow][playerCol - 1] is None:
            # Hallway to the right of an empty space
            available.remove("LEFT")
        elif current_player.isInRoom() and len(tilemap[playerRow][playerCol - 1]) != 0:
            # Hallway to the left is blocked
            available.remove("LEFT")

        return available
    
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
                        id="PlayerID",
                        x=(SCREEN_WIDTH // 4) * 3,
                        y=(SCREEN_HEIGHT // 4),
                        width=180,
                        height=60,
                        borderThickness=0,
                        borderRadius=12,
                        borderColor=Color.BLACK,
                        inactiveFillColor=Color.BLACK,
                        activeFillColor=Color.BLACK,
                        text=f"You are {self.model.game.getCurrentPlayer().getName()}",
                        # text=f"{vars(self.model.game)}",
                        textColor=Color.BLACK,
                        textHighlight=None,
                        font=Font.DEFAULT,
                        active=False,
                    )
                )

                #########################
                # ADD TURN BUTTONS HERE #
                #########################
                self.components.append(
                    MovementButton(
                        id="UpButton",
                        x=(SCREEN_WIDTH // 8) * 5,
                        y=(SCREEN_HEIGHT // 2),
                        direction="UP",
                        is_arrow=True,
                        width=70,
                        height=70,
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
                self.components.append(
                    MovementButton(
                        id="DownButton",
                        x=(SCREEN_WIDTH // 8) * 5,
                        y=(SCREEN_HEIGHT // 4) * 3,
                        direction="DOWN",
                        is_arrow=True,
                        width=70,
                        height=70,
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
                self.components.append(
                    MovementButton(
                        id="RightButton",
                        x=(SCREEN_WIDTH // 16) * 11,
                        y=(SCREEN_HEIGHT // 8) * 5,
                        direction="RIGHT",
                        is_arrow=True,
                        width=70,
                        height=70,
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
                self.components.append(
                    MovementButton(
                        id="LeftButton",
                        x=(SCREEN_WIDTH // 16) * 9,
                        y=(SCREEN_HEIGHT // 8) * 5,
                        direction="LEFT",
                        is_arrow=True,
                        width=70,
                        height=70,
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
                self.components.append(
                    MovementButton(
                        id="StayButton",
                        x=(SCREEN_WIDTH // 8) * 5,
                        y=(SCREEN_HEIGHT // 8) * 5,
                        direction="STAY",
                        is_arrow=False,
                        width=70,
                        height=70,
                        borderThickness=2,
                        borderRadius=12,
                        borderColor=Color.BLACK,
                        inactiveFillColor=Color.DARK_GRAY,
                        activeFillColor=Color.GREEN,
                        text="Stay",
                        textColor=Color.BLACK,
                        textHighlight=None,
                        font=Font.DEFAULT,
                        active=True,
                    )
                )
                self.components.append(
                    Button(
                        id="SuggestionButton",
                        x=(SCREEN_WIDTH // 16) * 13,
                        y=(SCREEN_HEIGHT // 2),
                        width=200,
                        height=70,
                        borderThickness=2,
                        borderRadius=12,
                        borderColor=Color.BLACK,
                        inactiveFillColor=Color.DARK_GRAY,
                        activeFillColor=Color.GREEN,
                        text="Suggest",
                        textColor=Color.BLACK,
                        textHighlight=None,
                        font=Font.DEFAULT,
                        active=False,
                    )
                )
                self.components.append(
                    Button(
                        id="SubmitButton",
                        x=(SCREEN_WIDTH // 16) * 13,
                        y=(SCREEN_HEIGHT // 4) * 3,
                        width=200,
                        height=70,
                        borderThickness=2,
                        borderRadius=12,
                        borderColor=Color.BLACK,
                        inactiveFillColor=Color.DARK_GRAY,
                        activeFillColor=Color.GREEN,
                        text="Submit Turn",
                        textColor=Color.BLACK,
                        textHighlight=None,
                        font=Font.DEFAULT,
                        active=False,
                    )
                )

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

    def openSuggestionMenu(self, room):
        menu = SuggestionMenu(
            room,
            x=SCREEN_WIDTH//2,
            y=SCREEN_HEIGHT//2
        )

        return menu.open(self.screen)