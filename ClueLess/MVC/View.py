import pygame

from ClueLess.MVC.GuiComponents import Button, Color, Constant, Font, Text
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
        self.screen = pygame.display.set_mode((Constant.WIDTH, Constant.HEIGHT))
        pygame.display.set_caption("Clue-Less")

        # Components to draw on screen
        self.components = []

    def getTargetComponent(self, point):
        """
        Gets the target component of the given point

        Parameters:
            point (tuple):
                The x and y coordinates of a point to find a component at
        """
        for component in self.components:
            if component.getArea().collidepoint(point):
                return component

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
                    x=Constant.WIDTH // 2,
                    y=150,
                    text="Clue-Less",
                    textColor=Color.BLACK,
                    textHighlight=None,
                    font=Font.DEFAULT,
                )
            )

            # Buttons
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
                    fillColor=Color.GRAY,
                    text="Quit",
                    textColor=Color.BLACK,
                    textHighlight=None,
                    font=Font.DEFAULT,
                )
            )
            self.components.append(
                Button(
                    id="HostButton",
                    x=Constant.WIDTH // 3,
                    y=(Constant.HEIGHT // 3) * 2,
                    width=180,
                    height=60,
                    borderThickness=2,
                    borderRadius=12,
                    borderColor=Color.BLACK,
                    fillColor=Color.GRAY,
                    text="Host",
                    textColor=Color.BLACK,
                    textHighlight=None,
                    font=Font.DEFAULT,
                )
            )
            self.components.append(
                Button(
                    id="JoinButton",
                    x=(Constant.WIDTH // 3) * 2,
                    y=(Constant.HEIGHT // 3) * 2,
                    width=180,
                    height=60,
                    borderThickness=2,
                    borderRadius=12,
                    borderColor=Color.BLACK,
                    fillColor=Color.GRAY,
                    text="Join",
                    textColor=Color.BLACK,
                    textHighlight=None,
                    font=Font.DEFAULT,
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
                    x=Constant.WIDTH // 2,
                    y=150,
                    text="Server Menu",
                    textColor=Color.BLACK,
                    textHighlight=None,
                    font=Font.DEFAULT,
                )
            )

            # Counts
            self.components.append(
                Text(
                    id="Counts",
                    x=Constant.WIDTH // 2,
                    y=200,
                    text=f"Red: {self.model.game.red} Green: {self.model.game.green}",
                    textColor=Color.BLACK,
                    textHighlight=None,
                    font=Font.DEFAULT,
                )
            )

            # Buttons
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
                    fillColor=Color.GRAY,
                    text="Back",
                    textColor=Color.BLACK,
                    textHighlight=None,
                    font=Font.DEFAULT,
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
                    x=Constant.WIDTH // 2,
                    y=150,
                    text="Client Menu",
                    textColor=Color.BLACK,
                    textHighlight=None,
                    font=Font.DEFAULT,
                )
            )

            # Counts
            self.components.append(
                Text(
                    id="Counts",
                    x=Constant.WIDTH // 2,
                    y=200,
                    text=f"Red: {self.model.game.red} Green: {self.model.game.green}",
                    textColor=Color.BLACK,
                    textHighlight=None,
                    font=Font.DEFAULT,
                )
            )

            # Buttons
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
                    fillColor=Color.GRAY,
                    text="Back",
                    textColor=Color.BLACK,
                    textHighlight=None,
                    font=Font.DEFAULT,
                )
            )

            # Buttons
            self.components.append(
                Button(
                    id="RedButton",
                    x=(Constant.WIDTH // 3),
                    y=(Constant.HEIGHT // 3) * 2,
                    width=180,
                    height=60,
                    borderThickness=2,
                    borderRadius=12,
                    borderColor=Color.BLACK,
                    fillColor=Color.RED,
                    text="Red",
                    textColor=Color.BLACK,
                    textHighlight=None,
                    font=Font.DEFAULT,
                )
            )
            self.components.append(
                Button(
                    id="GreenButton",
                    x=(Constant.WIDTH // 3) * 2,
                    y=(Constant.HEIGHT // 3) * 2,
                    width=180,
                    height=60,
                    borderThickness=2,
                    borderRadius=12,
                    borderColor=Color.BLACK,
                    fillColor=Color.GREEN,
                    text="Green",
                    textColor=Color.BLACK,
                    textHighlight=None,
                    font=Font.DEFAULT,
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
        if self.model.gameState == GameState.GAME_MENU:
            pass

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
