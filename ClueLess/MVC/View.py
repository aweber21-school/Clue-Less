import pygame

from ClueLess.States import State


class Constant:
    """Constants"""

    # WIDTH = 1280
    # HEIGHT = 720
    WIDTH = 640
    HEIGHT = 480


class Color:
    """Colors"""

    WHITE = (255, 255, 255)
    LIGHT_GRAY = (235, 235, 235)
    GRAY = (200, 200, 200)
    DARK_GRAY = (100, 100, 100)
    BLACK = (0, 0, 0)
    RED = (200, 40, 40)
    GREEN = (40, 160, 80)


class View:
    """
    The View for the Clue-Less application

    The View class serves as the GUI for our Clue-Less application. It acts as
    the View in the Model-View-Controller (MVC) architecture.

    Attributes:
        clock (pygame.time.Clock):
            The clock to manage frame rate
        screen (pygame.display.Surface):
            The main display
        fonts (Dict):
            Dictionary containing predefined fonts
    """

    def __init__(self, model):
        """
        Initializes a new view

        Parameters:
            model (ClueLess.MVC.Model):
                The model to update this view with
        """
        self.model = model

        pygame.init()

        self.screen = pygame.display.set_mode((Constant.WIDTH, Constant.HEIGHT))
        pygame.display.set_caption("Clue-Less")
        self.clock = pygame.time.Clock()

        self.fonts = {}
        self.fonts["TITLE"] = pygame.font.Font(None, 48)
        self.fonts["BUTTON"] = pygame.font.Font(None, 28)

    def drawButton(self, screen, rect, text, fill, font):
        """
        Draws a button with the given parameters

        Parameters:
            screen (pygame.display.Surface):
                The screen to display the button on
            rect (pygame.Rect):
                The rectangle to represent the button
            text (str):
                The text to display on the button
            fill (tuple, Globals.Color):
                The background color for the button
            font (pygame.font.Font):
                The font to use for the button text
        """
        pygame.draw.rect(screen, fill, rect, border_radius=12)
        pygame.draw.rect(screen, Color.BLACK, rect, 2, border_radius=12)
        txt = font.render(text, True, Color.BLACK)
        screen.blit(txt, txt.get_rect(center=rect.center))

    def displayMainMenu(self):
        """Displays the main menu"""
        # Clean display
        self.screen.fill(Color.WHITE)

        # Title
        title = self.fonts["TITLE"].render("Clue-Less", True, Color.BLACK)
        self.screen.blit(title, (Constant.WIDTH // 2 - title.get_width() // 2, 150))

        # Create Buttons
        self.host_btn = pygame.Rect(
            Constant.WIDTH // 3 - 90,
            (Constant.HEIGHT // 3) * 2 - 30,
            180,
            60,
        )
        self.join_btn = pygame.Rect(
            (Constant.WIDTH // 3) * 2 - 90,
            (Constant.HEIGHT // 3) * 2 - 30,
            180,
            60,
        )

        # Draw Buttons
        self.drawButton(
            self.screen,
            self.host_btn,
            "Host",
            Color.GRAY,
            self.fonts["BUTTON"],
        )
        self.drawButton(
            self.screen,
            self.join_btn,
            "Join",
            Color.GRAY,
            self.fonts["BUTTON"],
        )

    def displayServerMenu(self):
        """Displays the server menu"""
        # Clean display
        self.screen.fill(Color.WHITE)

        # Title
        title = self.fonts["TITLE"].render("Server Menu", True, Color.BLACK)
        self.screen.blit(title, (Constant.WIDTH // 2 - title.get_width() // 2, 150))

        # Counts
        ctext = self.fonts["TITLE"].render(
            f"Red: {self.model.redCount} Green: {self.model.greenCount}",
            True,
            Color.BLACK,
        )
        self.screen.blit(ctext, (Constant.WIDTH // 2 - ctext.get_width() // 2, 200))

        # Create Buttons
        self.back_btn = pygame.Rect(30, 30, 100, 40)

        # Draw Buttons
        self.drawButton(
            self.screen,
            self.back_btn,
            "Back",
            Color.GRAY,
            self.fonts["BUTTON"],
        )

    def displayClientMenu(self):
        """Displays the client menu"""
        # Clean display
        self.screen.fill(Color.WHITE)

        # Title
        title = self.fonts["TITLE"].render("Client Menu", True, Color.BLACK)
        self.screen.blit(title, (Constant.WIDTH // 2 - title.get_width() // 2, 150))

        # Counts
        ctext = self.fonts["TITLE"].render(
            f"Red: {self.model.redCount} Green: {self.model.greenCount}",
            True,
            Color.BLACK,
        )
        self.screen.blit(ctext, (Constant.WIDTH // 2 - ctext.get_width() // 2, 200))

        # Create Buttons
        self.red_btn = pygame.Rect(
            Constant.WIDTH // 3 - 90,
            (Constant.HEIGHT // 3) * 2 - 30,
            180,
            60,
        )
        self.green_btn = pygame.Rect(
            (Constant.WIDTH // 3) * 2 - 90,
            (Constant.HEIGHT // 3) * 2 - 30,
            180,
            60,
        )
        self.back_btn = pygame.Rect(30, 30, 100, 40)

        # Draw Buttons
        self.drawButton(
            self.screen,
            self.red_btn,
            "RED",
            Color.RED,
            self.fonts["TITLE"],
        )
        self.drawButton(
            self.screen,
            self.green_btn,
            "GREEN",
            Color.GREEN,
            self.fonts["TITLE"],
        )
        self.drawButton(
            self.screen,
            self.back_btn,
            "Back",
            Color.GRAY,
            self.fonts["BUTTON"],
        )

    def closeView(self):
        pygame.quit()

    def updateView(self):
        """Updates the view"""
        if self.model.state == State.MAIN_MENU:
            self.displayMainMenu()
        elif self.model.state == State.SERVER_MENU:
            self.displayServerMenu()
        elif self.model.state == State.CLIENT_MENU:
            self.displayClientMenu()

        pygame.display.flip()
        self.clock.tick(60)
