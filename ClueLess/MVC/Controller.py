import pygame

from ClueLess.Events import CLIENT_MESSAGE_RECEIVED_EVENT, SERVER_MESSAGE_RECEIVED_EVENT
from ClueLess.States import State


class Controller:
    """
    The Controller for the Clue-Less application

    The Controller class serves as the mediator for our Clue-Less Model and
    View. It acts as the Controller in the Model-View-Controller (MVC)
    architecture.

    Attributes:
        model (ClueLess.MVC.Model):
            The game state of the application
        view.(ClueLess.MVC.View):
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

    def handleMainMenuInput(self, event):
        """
        Handles the main menu user input

        Parameters:
            event (pygame.event.Event):
                The Pygame event to handle
        """
        # Esc Button
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            return False

        # Mouse Button Clicked
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Left Mouse Button Clicked
            if event.button == 1:
                # Host Button
                if self.view.host_btn.collidepoint(event.pos):
                    print("Host Pressed")
                    self.network.startServer("localhost", 5555, 6)
                    self.model.updateState(State.SERVER_MENU)

                # Join Button
                elif self.view.join_btn.collidepoint(event.pos):
                    print("Join Pressed")
                    self.network.startClient("User", "localhost", 5555)
                    self.model.updateState(State.CLIENT_MENU)

        return True

    def handleServerMenuInput(self, event):
        """
        Handles the server menu user input

        Parameters:
            event (pygame.event.Event):
                The Pygame event to handle
        """
        # Esc Button
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            self.network.stopServer()
            self.model.updateState(State.MAIN_MENU)

        # Mouse Button Clicked
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Left Mouse Button Clicked
            if event.button == 1:
                # Back Button
                if self.view.back_btn.collidepoint(event.pos):
                    print("Back Pressed")
                    self.network.stopServer()
                    self.model.updateState(State.MAIN_MENU)

        # Server received message from Client
        elif event.type == CLIENT_MESSAGE_RECEIVED_EVENT:
            sender = event.sender
            message = event.message
            print((sender, message))
            # Example text: "RED:5|GREEN:3"
            if message.startswith("RED:"):
                parts = message.split("|")
                red = int(parts[0].split(":")[1])
                green = int(parts[1].split(":")[1])
                self.model.updateCounts(red, green)

        return True

    def handleClientMenuInput(self, event):
        """
        Handles the client menu user input

        Parameters:
            event (pygame.event.Event):
                The Pygame event to handle
        """
        # Esc Button
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            self.network.stopClient()
            self.model.updateState(State.MAIN_MENU)

        # Mouse Button Clicked
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Left Mouse Button Clicked
            if event.button == 1:
                if self.view.red_btn.collidepoint(event.pos):
                    print("Red Pressed")
                    self.network.sendToServer("User|RED")
                elif self.view.green_btn.collidepoint(event.pos):
                    print("Green Pressed")
                    self.network.sendToServer("User|GREEN")
                elif self.view.back_btn.collidepoint(event.pos):
                    print("Back Pressed")
                    self.network.stopClient()
                    self.model.updateState(State.MAIN_MENU)

        # Client received message from server
        elif event.type == SERVER_MESSAGE_RECEIVED_EVENT:
            sender = event.sender
            message = event.message
            print((sender, message))
            # Example text: "RED:5|GREEN:3"
            if message.startswith("RED:"):
                parts = message.split("|")
                red = int(parts[0].split(":")[1])
                green = int(parts[1].split(":")[1])
                self.model.updateCounts(red, green)

        return True

    def handleInput(self):
        """Handles the application input"""
        running = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif self.model.state == State.MAIN_MENU:
                if not self.handleMainMenuInput(event):
                    running = False
            elif self.model.state == State.SERVER_MENU:
                if not self.handleServerMenuInput(event):
                    running = False
            elif self.model.state == State.CLIENT_MENU:
                if not self.handleClientMenuInput(event):
                    running = False
        return running
