import pygame


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


class Font:
    """Fonts"""

    pygame.font.init()
    DEFAULT = pygame.font.Font(None, 32)
    TITLE = pygame.font.Font(None, 48)
    BUTTON = pygame.font.Font(None, 28)


class Text:
    """
    A Text Component for Clue-Less View
    
    The Text class acts as text for the view in the Clue-Less application.

    Attributes:
        id (str):
            The id of the text component
        x (int):
            The x position
        y (int):
            The y position
        text (str):
            The string of text
        textColor (ClueLess.MVC.Color):
            The color of the text
        textHighlight (ClueLess.MVC.Color):
            The highlight of the text
        font (ClueLess.MVC.Font):
            The font of the text
    """
    def __init__(
        self,
        id,
        x,
        y,
        text="Text",
        textColor=Color.BLACK,
        textHighlight=None,
        font=Font.DEFAULT,
    ):
        """
        Initializes a new text component

        Parameters:
            id (str):
                The id of the text component
            x (int):
                The x position
            y (int):
                The y position
            text (str):
                The string of text
            textColor (ClueLess.MVC.Color):
                The color of the text
            textHighlight (ClueLess.MVC.Color):
                The highlight of the text
            font (ClueLess.MVC.Font):
                The font of the text
        """
        # ID
        self.id = id

        # Position
        self.x = x
        self.y = y

        # Text
        self.text = text
        self.textColor = textColor
        self.textHighlight = textHighlight
        self.font = font

    def getArea(self):
        """Gets the area of the component"""
        return self.font.render(
            self.text, True, self.textColor, self.textHighlight
        ).get_rect()

    def draw(self, surface):
        """Draws the component"""
        renderedText = self.font.render(
            self.text, True, self.textColor, self.textHighlight
        )
        surface.blit(
            renderedText,
            (
                self.x - (renderedText.get_width() // 2),
                self.y - (renderedText.get_height() // 2),
            ),
            None,
            0,
        )


class Button:
    """
    A Button Component for Clue-Less View
    
    The Button class acts as button for the view in the Clue-Less application.

    Attributes:
        id (str):
            The id of the text component
        x (int):
            The x position
        y (int):
            The y position
        width (int):
            The width
        height (int):
            The height
        borderThickness (int):
            The thickness of the border
        borderRadius (int):
            The radius of the border
        borderColor (ClueLess.MVC.Color):
            The color of the border
        fillColor (ClueLess.MVC.Color):
            The color to fill the background
        text (str):
            The string of text
        textColor (ClueLess.MVC.Color):
            The color of the text
        textHighlight (ClueLess.MVC.Color):
            The highlight of the text
        font (ClueLess.MVC.Font):
            The font of the text
    """
    def __init__(
        self,
        id,
        x,
        y,
        width=180,
        height=60,
        borderThickness=2,
        borderRadius=12,
        borderColor=Color.BLACK,
        fillColor=Color.GRAY,
        text="Button",
        textColor=Color.BLACK,
        textHighlight=None,
        font=Font.DEFAULT,
    ):
        """
        Initializes a new button component

        Parameters:
            id (str):
                The id of the text component
            x (int):
                The x position
            y (int):
                The y position
            width (int):
                The width
            height (int):
                The height
            borderThickness (int):
                The thickness of the border
            borderRadius (int):
                The radius of the border
            borderColor (ClueLess.MVC.Color):
                The color of the border
            fillColor (ClueLess.MVC.Color):
                The color to fill the background
            text (str):
                The string of text
            textColor (ClueLess.MVC.Color):
                The color of the text
            textHighlight (ClueLess.MVC.Color):
                The highlight of the text
            font (ClueLess.MVC.Font):
                The font of the text
        """
        # ID
        self.id = id

        # Position and size
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        # Border
        self.borderThickness = borderThickness
        self.borderRadius = borderRadius
        self.borderColor = borderColor

        # Fill
        self.fillColor = fillColor

        # Text
        self.text = text
        self.textColor = textColor
        self.textHighlight = textHighlight
        self.font = font

    def getArea(self):
        """Gets the area of the component"""
        return pygame.Rect(
            self.x - (self.width // 2),
            self.y - (self.height // 2),
            self.width,
            self.height,
        )

    def draw(self, surface):
        """Draws the component"""
        # Main rectangle
        pygame.draw.rect(
            surface,
            self.fillColor,
            pygame.Rect(
                self.x - (self.width // 2),
                self.y - (self.height // 2),
                self.width,
                self.height,
            ),
            0,
            self.borderRadius,
        )

        # Border
        pygame.draw.rect(
            surface,
            self.borderColor,
            pygame.Rect(
                self.x - (self.width // 2),
                self.y - (self.height // 2),
                self.width,
                self.height,
            ),
            self.borderThickness,
            self.borderRadius,
        )

        # Text
        renderedText = self.font.render(
            self.text, True, self.textColor, self.textHighlight
        )
        surface.blit(
            renderedText,
            (
                self.x - (renderedText.get_width() // 2),
                self.y - (renderedText.get_height() // 2),
            ),
            None,
            0,
        )
