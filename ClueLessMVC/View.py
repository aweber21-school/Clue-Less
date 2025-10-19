import pygame

from Globals import Color, Constant, State


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

    def __init__(self):
        """Initializes a new View"""
        pygame.init()

        self.screen = pygame.display.set_mode((Constant.WIDTH, Constant.HEIGHT))
        pygame.display.set_caption('Clue-Less')
        self.clock = pygame.time.Clock()

        self.fonts = {}
        self.fonts['TITLE'] = pygame.font.Font(None, 48)
        self.fonts['BUTTON'] = pygame.font.Font(None, 28)

    def drawButton(self, screen, rect, text, fill, font):
        """
        Draws a button with the given parameters

        Args:
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
        """Displays the Main Menu"""
        # Clean display
        self.screen.fill(Color.WHITE)

        # Title
        title = self.fonts['TITLE'].render('Clue-Less', True, Color.BLACK)
        self.screen.blit(
            title, (Constant.WIDTH // 2 - title.get_width() // 2, 150)
        )

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
            'Host',
            Color.GRAY,
            self.fonts['BUTTON'],
        )
        self.drawButton(
            self.screen,
            self.join_btn,
            'Join',
            Color.GRAY,
            self.fonts['BUTTON'],
        )

    def displayServerMenu(self, app):
        """Displays the Server Menu"""
        # Clean display
        self.screen.fill(Color.WHITE)

        # Title
        title = self.fonts['TITLE'].render('Server Menu', True, Color.BLACK)
        self.screen.blit(
            title, (Constant.WIDTH // 2 - title.get_width() // 2, 150)
        )

        # Counts
        ctext = self.fonts['TITLE'].render(f"Red: {app.role.getObj().counts["RED"]} Green: {app.role.getObj().counts["GREEN"]}", True, Color.BLACK)
        self.screen.blit(ctext, (Constant.WIDTH // 2 - ctext.get_width() // 2, 200))

        # Create Buttons
        self.back_btn = pygame.Rect(30, 30, 100, 40)

        # Draw Buttons
        self.drawButton(
            self.screen,
            self.back_btn,
            'Back',
            Color.GRAY,
            self.fonts['BUTTON'],
        )

    def displayClientMenu(self, controller):
        """Displays the Client Menu"""
        # Clean display
        self.screen.fill(Color.WHITE)

        # Title
        title = self.fonts['TITLE'].render('Client Menu', True, Color.BLACK)
        self.screen.blit(
            title, (Constant.WIDTH // 2 - title.get_width() // 2, 150)
        )

        # Counts
        ctext = self.fonts['TITLE'].render(f"Red: {controller.red_count} Green: {controller.green_count}", True, Color.BLACK)
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
            'RED',
            Color.RED,
            self.fonts['TITLE'],
        )
        self.drawButton(
            self.screen,
            self.green_btn,
            'GREEN',
            Color.GREEN,
            self.fonts['TITLE'],
        )
        self.drawButton(
            self.screen,
            self.back_btn,
            'Back',
            Color.GRAY,
            self.fonts['BUTTON'],
        )

    def closeView(self):
        pygame.quit()

    def updateView(self, app, model, controller):
        """
        Updates the View

        Args:
            app (Application):
                The top-level Clue-Less application
            model (ClueLessMVC.Model):
                The game state to display
            controller (ClueLessMVC.Controller):
                The controller in the MVC design
        """
        if model.state == State.MAIN_MENU:
            self.displayMainMenu()
        elif model.state == State.SERVER_MENU:
            self.displayServerMenu(app)
        elif model.state == State.CLIENT_MENU:
            self.displayClientMenu(controller)

        pygame.display.flip()
        self.clock.tick(60)
