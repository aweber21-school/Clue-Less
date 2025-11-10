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
            fill = (
                self.textColor
                if (self.active and self.isAvailable)
                else self.borderColor
            )
            pygame.draw.polygon(surface, fill, pts)
            # optional: crisp outline
            pygame.draw.polygon(surface, self.borderColor, pts, 1)
        else:
            # label mode (e.g., "Stay")
            rendered = self.font.render(
                self.text, True, self.textColor, self.textHighlight
            )
            surface.blit(
                rendered,
                (
                    self.x - (rendered.get_width() // 2),
                    self.y - (rendered.get_height() // 2),
                ),
            )


class SuggestionMenu:
    """
    Suggestion (suspect, weapon).
    Room is passed in (auto-populated).
    """

    def __init__(
        self,
        room,
        x=0,
        y=0,
        width=1180,
        height=680,
        borderThickness=2,
        borderRadius=12,
        borderColor=Color.BLACK,
        fillColor=Color.GRAY,
    ):
        # Shape
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.borderThickness = borderThickness
        self.borderRadius = borderRadius
        self.borderColor = borderColor
        self.fillColor = fillColor

        # Layout
        self.text = self.initialize_text(room)
        self.navigation_buttons = self.initialize_buttons()
        self.suspect_buttons = self.initialize_suspect_buttons()
        self.weapon_buttons = self.initialize_weapon_buttons()
        self.all_buttons = (
            self.navigation_buttons + self.suspect_buttons + self.weapon_buttons
        )

        # State
        self.selected_suspect = None
        self.selected_weapon = None
        self.selected_room = room

    def initialize_text(self, room):
        text = []
        text.append(
            Text(
                id="SuggestionText",
                x=self.x,
                y=self.y - (self.height // 8) * 3,
                text="Suggestion",
            )
        )
        text.append(
            Text(
                id="SuspectText",
                x=self.x - (self.width // 16) * 7,
                y=self.y - (self.height // 4),
                text="Suspect:",
            )
        )
        text.append(
            Text(
                id="WeaponText",
                x=self.x - (self.width // 16) * 7,
                y=self.y,
                text="Weapon:",
            )
        )
        text.append(
            Text(
                id="RoomText",
                x=self.x,
                y=self.y + (self.height // 4),
                text=f"Room: {room}",
            )
        )

        return text

    def initialize_buttons(self):
        buttons = []
        buttons.append(
            Button(
                "SuggestionSubmitButton",
                x=self.x + (self.width // 8) * 3,
                y=self.y + (self.height // 8) * 3,
                text="Submit",
                active=False,
            )
        )

        buttons.append(
            Button(
                "BackButton",
                x=self.x - (self.width // 16) * 7,
                y=self.y - (self.height // 16) * 7,
                width=100,
                height=40,
                text="Back",
                active=True,
            )
        )
        return buttons

    def initialize_suspect_buttons(self):
        buttons = []
        buttons.append(
            Button(
                "MissScarlett",
                x=self.x - (self.width // 16) * 5,
                y=self.y - (self.height // 4),
                width=140,
                text="Scarlett",
                active=False,
            )
        )
        buttons.append(
            Button(
                "ColonelMustard",
                x=self.x - (self.width // 16) * 3,
                y=self.y - (self.height // 4),
                width=140,
                text="Mustard",
                active=False,
            )
        )
        buttons.append(
            Button(
                "MrsWhite",
                x=self.x - (self.width // 16),
                y=self.y - (self.height // 4),
                width=140,
                text="White",
                active=False,
            )
        )
        buttons.append(
            Button(
                "MrGreen",
                x=self.x + (self.width // 16),
                y=self.y - (self.height // 4),
                width=140,
                text="Green",
                active=False,
            )
        )
        buttons.append(
            Button(
                "MrsPeacock",
                x=self.x + (self.width // 16) * 3,
                y=self.y - (self.height // 4),
                width=140,
                text="Peacock",
                active=False,
            )
        )
        buttons.append(
            Button(
                "ProfessorPlum",
                x=self.x + (self.width // 16) * 5,
                y=self.y - (self.height // 4),
                width=140,
                text="Plum",
                active=False,
            )
        )

        return buttons

    def initialize_weapon_buttons(self):
        buttons = []

        buttons.append(
            Button(
                "Candlestick",
                x=self.x - (self.width // 16) * 5,
                y=self.y,
                width=140,
                text="Candlestick",
                active=False,
            )
        )
        buttons.append(
            Button(
                "Dagger",
                x=self.x - (self.width // 16) * 3,
                y=self.y,
                width=140,
                text="Dagger",
                active=False,
            )
        )
        buttons.append(
            Button(
                "LeadPipe",
                x=self.x - (self.width // 16),
                y=self.y,
                width=140,
                text="Lead Pipe",
                active=False,
            )
        )
        buttons.append(
            Button(
                "Revolver",
                x=self.x + (self.width // 16),
                y=self.y,
                width=140,
                text="Revolver",
                active=False,
            )
        )
        buttons.append(
            Button(
                "Rope",
                x=self.x + (self.width // 16) * 3,
                y=self.y,
                width=140,
                text="Rope",
                active=False,
            )
        )
        buttons.append(
            Button(
                "Wrench",
                x=self.x + (self.width // 16) * 5,
                y=self.y,
                width=140,
                text="Wrench",
                active=False,
            )
        )

        return buttons

    def draw(self, surface):
        # Draw the fill and the border
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

        for text in self.text:
            text.draw(surface)

        for button in self.navigation_buttons:
            button.draw(surface)

        for button in self.suspect_buttons:
            button.draw(surface)

        for button in self.weapon_buttons:
            button.draw(surface)

        pygame.display.flip()

    def getClickedComponent(self, point):
        """
        Gets the clicked component of the given point

        Parameters:
            point (tuple):
                The x and y coordinates of a point to find a component at
        """
        for component in self.all_buttons:
            if component.getArea().collidepoint(point):
                return component

    def enableComponent(self, component_name):
        for component in self.all_buttons:
            if component.id == component_name:
                component.active = True

    def open(self, surface):
        """Run a blocking loop until submit/cancel. Returns dict or None."""
        clock = pygame.time.Clock()
        running = True
        result = None

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # bubble up quit; treat as cancel so caller can handle app shutdown separately
                    running = False
                    result = None
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                        result = None
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Mouse button clicked
                    if event.button == 1:
                        # Left mouse button clicked
                        component = self.getClickedComponent(event.pos)
                        if component is not None:
                            # A component was clicked
                            if component.id == "BackButton":
                                running = False
                                result = None
                            elif (
                                component.id == "SuggestionSubmitButton"
                                and component.active
                            ):
                                running = False
                                result = (
                                    self.selected_suspect,
                                    self.selected_weapon,
                                    self.selected_room,
                                )
                            elif component in self.suspect_buttons:
                                if not component.active:
                                    # Enable this component and update self.selected_suspect, disable all other suspects
                                    self.selected_suspect = component.id
                                    for other_component in self.suspect_buttons:
                                        other_component.active = False
                                    component.active = True
                            elif component in self.weapon_buttons:
                                if not component.active:
                                    # Enable this component and update self.selected_weapon, disable all other weapons
                                    self.selected_weapon = component.id
                                    for other_component in self.weapon_buttons:
                                        other_component.active = False
                                    component.active = True
                            else:
                                # Any other component was clicked
                                pass
                    elif event.button == 2:
                        # Right mouse button clicked
                        pass

                    else:
                        # Any other mouse button clicked
                        pass

            if self.selected_suspect is not None and self.selected_weapon is not None:
                self.enableComponent("SuggestionSubmitButton")

            self.draw(surface)
            clock.tick(60)

        return result


class AccusationMenu:
    """
    Suggestion (suspect, weapon, room).
    """

    def __init__(
        self,
        x=0,
        y=0,
        width=1180,
        height=680,
        borderThickness=2,
        borderRadius=12,
        borderColor=Color.BLACK,
        fillColor=Color.GRAY,
    ):
        # Shape
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.borderThickness = borderThickness
        self.borderRadius = borderRadius
        self.borderColor = borderColor
        self.fillColor = fillColor

        # Layout
        self.text = self.initialize_text()
        self.navigation_buttons = self.initialize_buttons()
        self.suspect_buttons = self.initialize_suspect_buttons()
        self.weapon_buttons = self.initialize_weapon_buttons()
        self.room_buttons = self.initialize_room_buttons()
        self.all_buttons = (
            self.navigation_buttons
            + self.suspect_buttons
            + self.weapon_buttons
            + self.room_buttons
        )

        # State
        self.selected_suspect = None
        self.selected_weapon = None
        self.selected_room = None

    def initialize_text(self):
        text = []
        text.append(
            Text(
                id="SuggestionText",
                x=self.x,
                y=self.y - (self.height // 8) * 3,
                text="Suggestion",
            )
        )
        text.append(
            Text(
                id="SuspectText",
                x=self.x - (self.width // 16) * 7,
                y=self.y - (self.height // 4),
                text="Suspect:",
            )
        )
        text.append(
            Text(
                id="WeaponText",
                x=self.x - (self.width // 16) * 7,
                y=self.y,
                text="Weapon:",
            )
        )
        text.append(
            Text(
                id="RoomText",
                x=self.x - (self.width // 16) * 7,
                y=self.y + (self.height // 4),
                text="Room:",
            )
        )

        return text

    def initialize_buttons(self):
        buttons = []
        buttons.append(
            Button(
                "SuggestionSubmitButton",
                x=self.x + (self.width // 8) * 3,
                y=self.y + (self.height // 8) * 3,
                text="Submit",
                active=False,
            )
        )

        buttons.append(
            Button(
                "BackButton",
                x=self.x - (self.width // 16) * 7,
                y=self.y - (self.height // 16) * 7,
                width=100,
                height=40,
                text="Back",
                active=True,
            )
        )
        return buttons

    def initialize_suspect_buttons(self):
        buttons = []
        buttons.append(
            Button(
                "MissScarlett",
                x=self.x - (self.width // 16) * 5,
                y=self.y - (self.height // 4),
                width=140,
                text="Scarlett",
                active=False,
            )
        )
        buttons.append(
            Button(
                "ColonelMustard",
                x=self.x - (self.width // 16) * 3,
                y=self.y - (self.height // 4),
                width=140,
                text="Mustard",
                active=False,
            )
        )
        buttons.append(
            Button(
                "MrsWhite",
                x=self.x - (self.width // 16),
                y=self.y - (self.height // 4),
                width=140,
                text="White",
                active=False,
            )
        )
        buttons.append(
            Button(
                "MrGreen",
                x=self.x + (self.width // 16),
                y=self.y - (self.height // 4),
                width=140,
                text="Green",
                active=False,
            )
        )
        buttons.append(
            Button(
                "MrsPeacock",
                x=self.x + (self.width // 16) * 3,
                y=self.y - (self.height // 4),
                width=140,
                text="Peacock",
                active=False,
            )
        )
        buttons.append(
            Button(
                "ProfessorPlum",
                x=self.x + (self.width // 16) * 5,
                y=self.y - (self.height // 4),
                width=140,
                text="Plum",
                active=False,
            )
        )

        return buttons

    def initialize_weapon_buttons(self):
        buttons = []

        buttons.append(
            Button(
                "Candlestick",
                x=self.x - (self.width // 16) * 5,
                y=self.y,
                width=140,
                text="Candlestick",
                active=False,
            )
        )
        buttons.append(
            Button(
                "Dagger",
                x=self.x - (self.width // 16) * 3,
                y=self.y,
                width=140,
                text="Dagger",
                active=False,
            )
        )
        buttons.append(
            Button(
                "LeadPipe",
                x=self.x - (self.width // 16),
                y=self.y,
                width=140,
                text="Lead Pipe",
                active=False,
            )
        )
        buttons.append(
            Button(
                "Revolver",
                x=self.x + (self.width // 16),
                y=self.y,
                width=140,
                text="Revolver",
                active=False,
            )
        )
        buttons.append(
            Button(
                "Rope",
                x=self.x + (self.width // 16) * 3,
                y=self.y,
                width=140,
                text="Rope",
                active=False,
            )
        )
        buttons.append(
            Button(
                "Wrench",
                x=self.x + (self.width // 16) * 5,
                y=self.y,
                width=140,
                text="Wrench",
                active=False,
            )
        )

        return buttons

    def initialize_room_buttons(self):
        buttons = []

        buttons.append(
            Button(
                "Study",
                x=self.x - (self.width // 16) * 5,
                y=self.y + (self.height // 4),
                width=140,
                text="Study",
                active=False,
            )
        )
        buttons.append(
            Button(
                "Hall",
                x=self.x - (self.width // 16) * 3,
                y=self.y + (self.height // 4),
                width=140,
                text="Hall",
                active=False,
            )
        )
        buttons.append(
            Button(
                "Lounge",
                x=self.x - (self.width // 16),
                y=self.y + (self.height // 4),
                width=140,
                text="Lounge",
                active=False,
            )
        )
        buttons.append(
            Button(
                "Library",
                x=self.x + (self.width // 16),
                y=self.y + (self.height // 4),
                width=140,
                text="Library",
                active=False,
            )
        )
        buttons.append(
            Button(
                "Billiard",
                x=self.x + (self.width // 16) * 3,
                y=self.y + (self.height // 4),
                width=140,
                text="Billiard",
                active=False,
            )
        )
        buttons.append(
            Button(
                "Conservatory",
                x=self.x - (self.width // 16) * 5,
                y=self.y + (self.height // 8) * 3,
                width=140,
                text="Conservatory",
                active=False,
            )
        )
        buttons.append(
            Button(
                "Ballroom",
                x=self.x - (self.width // 16) * 3,
                y=self.y + (self.height // 8) * 3,
                width=140,
                text="Ballroom",
                active=False,
            )
        )
        buttons.append(
            Button(
                "Kitchen",
                x=self.x - (self.width // 16),
                y=self.y + (self.height // 8) * 3,
                width=140,
                text="Kitchen",
                active=False,
            )
        )
        return buttons

    def draw(self, surface):
        # Draw the fill and the border
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

        for text in self.text:
            text.draw(surface)

        for button in self.navigation_buttons:
            button.draw(surface)

        for button in self.suspect_buttons:
            button.draw(surface)

        for button in self.weapon_buttons:
            button.draw(surface)

        for button in self.room_buttons:
            button.draw(surface)

        pygame.display.flip()

    def getClickedComponent(self, point):
        """
        Gets the clicked component of the given point

        Parameters:
            point (tuple):
                The x and y coordinates of a point to find a component at
        """
        for component in self.all_buttons:
            if component.getArea().collidepoint(point):
                return component

    def enableComponent(self, component_name):
        for component in self.all_buttons:
            if component.id == component_name:
                component.active = True

    def open(self, surface):
        """Run a blocking loop until submit/cancel. Returns dict or None."""
        clock = pygame.time.Clock()
        running = True
        result = None

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # bubble up quit; treat as cancel so caller can handle app shutdown separately
                    running = False
                    result = None
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                        result = None
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Mouse button clicked
                    if event.button == 1:
                        # Left mouse button clicked
                        component = self.getClickedComponent(event.pos)
                        if component is not None:
                            # A component was clicked
                            if component.id == "BackButton":
                                running = False
                                result = None
                            elif (
                                component.id == "SuggestionSubmitButton"
                                and component.active
                            ):
                                running = False
                                result = (
                                    self.selected_suspect,
                                    self.selected_weapon,
                                    self.selected_room,
                                )
                            elif component in self.suspect_buttons:
                                if not component.active:
                                    # Enable this component and update self.selected_suspect, disable all other suspects
                                    self.selected_suspect = component.id
                                    for other_component in self.suspect_buttons:
                                        other_component.active = False
                                    component.active = True
                            elif component in self.weapon_buttons:
                                if not component.active:
                                    # Enable this component and update self.selected_weapon, disable all other weapons
                                    self.selected_weapon = component.id
                                    for other_component in self.weapon_buttons:
                                        other_component.active = False
                                    component.active = True
                            elif component in self.room_buttons:
                                if not component.active:
                                    # Enable this component and update self.selected_weapon, disable all other weapons
                                    self.selected_room = component.id
                                    for other_component in self.room_buttons:
                                        other_component.active = False
                                    component.active = True
                            else:
                                # Any other component was clicked
                                pass
                    elif event.button == 2:
                        # Right mouse button clicked
                        pass

                    else:
                        # Any other mouse button clicked
                        pass

            if (
                self.selected_suspect is not None
                and self.selected_weapon is not None
                and self.selected_room is not None
            ):
                self.enableComponent("SuggestionSubmitButton")

            self.draw(surface)
            clock.tick(60)

        return result
