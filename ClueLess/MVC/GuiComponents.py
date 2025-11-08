"""GUI Components for the Clue-Less Application"""

import pygame

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720


class Color:
    """Colors"""

    WHITE = (255, 255, 255)
    LIGHT_GRAY = (235, 235, 235)
    GRAY = (200, 200, 200)
    DARK_GRAY = (100, 100, 100)
    LIGHT_BROWN = (210, 180, 140)
    BROWN = (160, 82, 45)
    DARK_BROWN = (139, 69, 19)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    ORANGE = (255, 140, 0)
    YELLOW = (255, 255, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    PURPLE = (128, 0, 128)


class Font:
    """Fonts"""

    pygame.font.init()
    DEFAULT = pygame.font.Font(None, 32)
    TITLE = pygame.font.Font(None, 48)
    BUTTON = pygame.font.Font(None, 28)


class Component:
    """
    A Component for Clue-Less View

    The Component class is a visual component for the view in the Clue-Less
    application.

    Attributes:
        id (string):
            The id of the component
        x (integer):
            The x position
        y (integer):
            The y position
        width (integer):
            The width
        height (integer):
            The height
        borderThickness (integer):
            The thickness of the border
        borderRadius (integer):
            The radius of the border
        borderColor (ClueLess.MVC.Color):
            The color of the border
        inactiveFillColor (ClueLess.MVC.Color):
            The color to fill the background when it is disabled
        activeFillColor (ClueLess.MVC.Color):
            The color to fill the background when it is enabled
        text (string):
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
        width,
        height,
        borderThickness,
        borderRadius,
        borderColor,
        inactiveFillColor,
        activeFillColor,
        text,
        textColor,
        textHighlight,
        font,
        active,
    ):
        """
        Initializes a new component

        Parameters:
            id (string):
                The id of the component
            x (integer):
                The x position
            y (integer):
                The y position
            width (integer):
                The width
            height (integer):
                The height
            borderThickness (integer):
                The thickness of the border
            borderRadius (integer):
                The radius of the border
            borderColor (ClueLess.MVC.Color):
                The color of the border
            inactiveFillColor (ClueLess.MVC.Color):
                The color to fill the background when it is disabled
            activeFillColor (ClueLess.MVC.Color):
                The color to fill the background when it is enabled
            text (string):
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
        """Gets the text of the component"""
        return self.text

    def updateText(self, event):
        """
        Updates the text of the component

        Parameters:
            event (string):
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


class Text(Component):
    """
    A Text Component for Clue-Less View

    The Text class acts as a text component for the view in the Clue-Less
    application.

    Implements:
        ClueLess.MVC.Component
    Attributes:
        id (string):
            The id of the component
        x (integer):
            The x position
        y (integer):
            The y position
        width (integer):
            The width
        height (integer):
            The height
        borderThickness (integer):
            The thickness of the border
        borderRadius (integer):
            The radius of the border
        borderColor (ClueLess.MVC.Color):
            The color of the border
        inactiveFillColor (ClueLess.MVC.Color):
            The color to fill the background when it is disabled
        activeFillColor (ClueLess.MVC.Color):
            The color to fill the background when it is enabled
        text (string):
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
        borderThickness=0,
        borderRadius=12,
        borderColor=Color.BLACK,
        inactiveFillColor=Color.BLACK,
        activeFillColor=Color.BLACK,
        text="Text",
        textColor=Color.BLACK,
        textHighlight=None,
        font=Font.DEFAULT,
        active=False,
    ):
        """
        Initializes a new text component

        Parameters:
        id (string):
            The id of the component
        x (integer):
            The x position
        y (integer):
            The y position
        width (integer):
            The width
        height (integer):
            The height
        borderThickness (integer):
            The thickness of the border
        borderRadius (integer):
            The radius of the border
        borderColor (ClueLess.MVC.Color):
            The color of the border
        inactiveFillColor (ClueLess.MVC.Color):
            The color to fill the background when it is disabled
        activeFillColor (ClueLess.MVC.Color):
            The color to fill the background when it is enabled
        text (string):
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
        super().__init__(
            id,
            x,
            y,
            width,
            height,
            borderThickness,
            borderRadius,
            borderColor,
            inactiveFillColor,
            activeFillColor,
            text,
            textColor,
            textHighlight,
            font,
            active,
        )

    def getArea(self):
        """Gets the area of the component"""
        return self.font.render(
            self.text, True, self.textColor, self.textHighlight
        ).get_rect()

    def draw(self, surface):
        """Draws the component"""
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
            self.borderThickness if self.borderThickness != 0 else -1,
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


class Box(Component):
    """
    A Box Component for Clue-Less View

    The Box class acts as a box component for the view in the Clue-Less
    application.

    Implements:
        ClueLess.MVC.Component
    Attributes:
        id (string):
            The id of the component
        x (integer):
            The x position
        y (integer):
            The y position
        width (integer):
            The width
        height (integer):
            The height
        borderThickness (integer):
            The thickness of the border
        borderRadius (integer):
            The radius of the border
        borderColor (ClueLess.MVC.Color):
            The color of the border
        inactiveFillColor (ClueLess.MVC.Color):
            The color to fill the background when it is disabled
        activeFillColor (ClueLess.MVC.Color):
            The color to fill the background when it is enabled
        text (string):
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
            id (string):
                The id of the component
            x (integer):
                The x position
            y (integer):
                The y position
            width (integer):
                The width
            height (integer):
                The height
            borderThickness (integer):
                The thickness of the border
            borderRadius (integer):
                The radius of the border
            borderColor (ClueLess.MVC.Color):
                The color of the border
            inactiveFillColor (ClueLess.MVC.Color):
                The color to fill the background when it is disabled
            activeFillColor (ClueLess.MVC.Color):
                The color to fill the background when it is enabled
            text (string):
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
        super().__init__(
            id,
            x,
            y,
            width,
            height,
            borderThickness,
            borderRadius,
            borderColor,
            inactiveFillColor,
            activeFillColor,
            text,
            textColor,
            textHighlight,
            font,
            active,
        )


class TextBox(Component):
    """
    A Text Box Component for Clue-Less View

    The Text Box class acts as a text box component for the view in the
    Clue-Less application.

    Implements:
        ClueLess.MVC.Component
    Attributes:
        id (string):
            The id of the component
        x (integer):
            The x position
        y (integer):
            The y position
        width (integer):
            The width
        height (integer):
            The height
        borderThickness (integer):
            The thickness of the border
        borderRadius (integer):
            The radius of the border
        borderColor (ClueLess.MVC.Color):
            The color of the border
        inactiveFillColor (ClueLess.MVC.Color):
            The color to fill the background when it is disabled
        activeFillColor (ClueLess.MVC.Color):
            The color to fill the background when it is enabled
        text (string):
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
        text="TextBox",
        textColor=Color.BLACK,
        textHighlight=None,
        font=Font.DEFAULT,
        active=False,
    ):
        """
        Initializes a new text box component

        Parameters:
            id (string):
                The id of the component
            x (integer):
                The x position
            y (integer):
                The y position
            width (integer):
                The width
            height (integer):
                The height
            borderThickness (integer):
                The thickness of the border
            borderRadius (integer):
                The radius of the border
            borderColor (ClueLess.MVC.Color):
                The color of the border
            inactiveFillColor (ClueLess.MVC.Color):
                The color to fill the background when it is disabled
            activeFillColor (ClueLess.MVC.Color):
                The color to fill the background when it is enabled
            text (string):
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
        super().__init__(
            id,
            x,
            y,
            width,
            height,
            borderThickness,
            borderRadius,
            borderColor,
            inactiveFillColor,
            activeFillColor,
            text,
            textColor,
            textHighlight,
            font,
            active,
        )

    def draw(self, surface):
        """Draws the component"""
        super().draw(surface)

        # Cursor
        if self.active:
            renderedText = self.font.render(
                self.text, True, self.textColor, self.textHighlight
            )
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


class Button(Component):
    """
    A Button Component for Clue-Less View

    The Button class acts as a button component for the view in the Clue-Less
    application.

    Implements:
        ClueLess.MVC.Component
    Attributes:
        id (string):
            The id of the component
        x (integer):
            The x position
        y (integer):
            The y position
        width (integer):
            The width
        height (integer):
            The height
        borderThickness (integer):
            The thickness of the border
        borderRadius (integer):
            The radius of the border
        borderColor (ClueLess.MVC.Color):
            The color of the border
        inactiveFillColor (ClueLess.MVC.Color):
            The color to fill the background when it is disabled
        activeFillColor (ClueLess.MVC.Color):
            The color to fill the background when it is enabled
        text (string):
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
            id (string):
                The id of the component
            x (integer):
                The x position
            y (integer):
                The y position
            width (integer):
                The width
            height (integer):
                The height
            borderThickness (integer):
                The thickness of the border
            borderRadius (integer):
                The radius of the border
            borderColor (ClueLess.MVC.Color):
                The color of the border
            inactiveFillColor (ClueLess.MVC.Color):
                The color to fill the background when it is disabled
            activeFillColor (ClueLess.MVC.Color):
                The color to fill the background when it is enabled
            text (string):
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
        super().__init__(
            id,
            x,
            y,
            width,
            height,
            borderThickness,
            borderRadius,
            borderColor,
            inactiveFillColor,
            activeFillColor,
            text,
            textColor,
            textHighlight,
            font,
            active,
        )

class MovementButton(Button):
    """
    A movement button that can either show an arrow (for moving) or a label like 'Stay'.

    Implements:
        ClueLess.MVC.Component
    Attributes:
        id (string):
            The id of the component
        x (integer):
            The x position
        y (integer):
            The y position
        direction (string):
            The direction this arrow button will face
        width (integer):
            The width
        height (integer):
            The height
        borderThickness (integer):
            The thickness of the border
        borderRadius (integer):
            The radius of the border
        borderColor (ClueLess.MVC.Color):
            The color of the border
        inactiveFillColor (ClueLess.MVC.Color):
            The color to fill the background when it is disabled
        activeFillColor (ClueLess.MVC.Color):
            The color to fill the background when it is enabled
        text (string):
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
        is_arrow=False,
        direction="UP",
        isAvailable=True,
        width=180,
        height=60,
        borderThickness=2,
        borderRadius=12,
        borderColor=Color.BLACK,
        inactiveFillColor=Color.DARK_GRAY,
        activeFillColor=Color.LIGHT_GRAY,
        text="Stay",
        textColor=Color.BLACK,
        textHighlight=None,
        font=Font.DEFAULT,
        active=False,
    ):
        """
        Initializes a new button component

        Parameters:
            id (string):
                The id of the component
            x (integer):
                The x position
            y (integer):
                The y position
            width (integer):
                The width
            height (integer):
                The height
            borderThickness (integer):
                The thickness of the border
            borderRadius (integer):
                The radius of the border
            borderColor (ClueLess.MVC.Color):
                The color of the border
            inactiveFillColor (ClueLess.MVC.Color):
                The color to fill the background when it is disabled
            activeFillColor (ClueLess.MVC.Color):
                The color to fill the background when it is enabled
            text (string):
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
        self.is_arrow = is_arrow
        self.direction = direction
        self.isAvailable = isAvailable
        super().__init__(
            id,
            x,
            y,
            width,
            height,
            borderThickness,
            borderRadius,
            borderColor,
            inactiveFillColor,
            activeFillColor,
            text,
            textColor,
            textHighlight,
            font,
            active,
        )

    def _triangle_points(self):
        """Return 3 points for a triangle centered at (self.x,self.y) facing self.direction."""
        x, y = self.x, self.y
        s = int(min(self.width, self.height) * 0.28)  # arrow size relative to button
        d = self.direction

        if d == "UP":
            return [(x, y - s), (x - s, y + s), (x + s, y + s)]
        if d == "DOWN":
            return [(x, y + s), (x - s, y - s), (x + s, y - s)]
        if d == "LEFT":
            return [(x - s, y), (x + s, y - s), (x + s, y + s)]
        # else "RIGHT"
        return [(x + s, y), (x - s, y - s), (x - s, y + s)]

    def draw(self, surface):
        """Draw the button background + border, then the arrow triangle."""
        # draw button chrome
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

        if self.is_arrow:
            # arrow mode
            pts = self._triangle_points()
            fill = self.textColor if (self.active and self.isAvailable) else self.borderColor
            pygame.draw.polygon(surface, fill, pts)
            # optional: crisp outline
            pygame.draw.polygon(surface, self.borderColor, pts, 1)
        else:
            # label mode (e.g., "Stay")
            rendered = self.font.render(self.text, True, self.textColor, self.textHighlight)
            surface.blit(
                rendered,
                (
                    self.x - (rendered.get_width() // 2),
                    self.y - (rendered.get_height() // 2),
                ),
            )