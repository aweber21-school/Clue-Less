import pygame


class Constant:
    """Constants"""

    WIDTH = 1280
    HEIGHT = 720


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

    def getID(self):
        """Returns the component's ID"""
        return self.id

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


class TextBox:
    """
    A Text Box Component for Clue-Less View

    The TextBox class acts as text for the view in the Clue-Less application.

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
        inactiveFillColor (ClueLess.MVC.Color):
            The color to fill the background when it is disabled
        activeFillColor (ClueLess.MVC.Color):
            The color to fill the background when it is enabled
        text (str):
            The string of text
        textColor (ClueLess.MVC.Color):
            The color of the text
        textHighlight (ClueLess.MVC.Color):
            The highlight of the text
        font (ClueLess.MVC.Font):
            The font of the text
        active (boolean):
            The flag to determine whether it is active
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
        inactiveFillColor=Color.DARK_GRAY,
        activeFillColor=Color.GRAY,
        text="Button",
        textColor=Color.BLACK,
        textHighlight=None,
        font=Font.DEFAULT,
        active=False,
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
            inactiveFillColor (ClueLess.MVC.Color):
                The color to fill the background when it is disabled
            activeFillColor (ClueLess.MVC.Color):
                The color to fill the background when it is enabled
            text (str):
                The string of text
            textColor (ClueLess.MVC.Color):
                The color of the text
            textHighlight (ClueLess.MVC.Color):
                The highlight of the text
            font (ClueLess.MVC.Font):
                The font of the text
            active (boolean):
                The flag to determine whether it is active
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
        self.inactiveFillColor = inactiveFillColor
        self.activeFillColor = activeFillColor

        # Text
        self.text = text
        self.textColor = textColor
        self.textHighlight = textHighlight
        self.font = font

        # Active
        self.active = active

    def getID(self):
        """Returns the component's ID"""
        return self.id

    def isActive(self):
        """Returns whether the component is active"""
        return self.active

    def activate(self):
        """Activates the component"""
        self.active = True

    def deactivate(self):
        """Deactivates the component"""
        self.active = False

    def getText(self):
        """Returns the text within the component"""
        return self.text

    def updateText(self, event):
        """
        Updates the text of the component

        Parameters:
            event (str):
                The event to use to update the component
        """
        if event.key == pygame.K_BACKSPACE:
            # Backspace
            self.text = self.text[:-1]
        else:
            # Any other key
            self.text += event.unicode

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
            self.activeFillColor if self.active else self.inactiveFillColor,
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

        # Cursor
        if self.active:
            pygame.draw.rect(
                surface,
                self.borderColor,
                pygame.Rect(
                    self.x + (renderedText.get_width() // 2),
                    self.y - (renderedText.get_height() // 2),
                    2,
                    renderedText.get_height(),
                ),
                0,
                self.borderRadius,
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
        inactiveFillColor (ClueLess.MVC.Color):
            The color to fill the background when it is disabled
        activeFillColor (ClueLess.MVC.Color):
            The color to fill the background when it is enabled
        text (str):
            The string of text
        textColor (ClueLess.MVC.Color):
            The color of the text
        textHighlight (ClueLess.MVC.Color):
            The highlight of the text
        font (ClueLess.MVC.Font):
            The font of the text
        active (boolean):
            The flag to determine whether it is active
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
        inactiveFillColor=Color.DARK_GRAY,
        activeFillColor=Color.LIGHT_GRAY,
        text="Button",
        textColor=Color.BLACK,
        textHighlight=None,
        font=Font.DEFAULT,
        active=False,
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
            inactiveFillColor (ClueLess.MVC.Color):
                The color to fill the background when it is disabled
            activeFillColor (ClueLess.MVC.Color):
                The color to fill the background when it is enabled
            text (str):
                The string of text
            textColor (ClueLess.MVC.Color):
                The color of the text
            textHighlight (ClueLess.MVC.Color):
                The highlight of the text
            font (ClueLess.MVC.Font):
                The font of the text
            active (boolean):
                The flag to determine whether it is active
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
        self.inactiveFillColor = inactiveFillColor
        self.activeFillColor = activeFillColor

        # Text
        self.text = text
        self.textColor = textColor
        self.textHighlight = textHighlight
        self.font = font

        # Active
        self.active = active

    def getID(self):
        """Returns the component's ID"""
        return self.id

    def isActive(self):
        """Returns whether the component is active"""
        return self.active

    def activate(self):
        """Activates the component"""
        self.active = True

    def deactivate(self):
        """Deactivates the component"""
        self.active = False

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
            self.activeFillColor if self.active else self.inactiveFillColor,
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
