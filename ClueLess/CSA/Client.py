import pickle
import socket

import pygame

from ClueLess.Events import (
    CLIENT_CONNECTED_EVENT,
    CLIENT_DISCONNECTED_EVENT,
    CLIENT_MESSAGE_RECEIVED_EVENT,
)


class Client:
    """
    The Client for the Clue-Less application

    The Client class acts as the client in the Client-Server architecture
    implemented for the Clue-Less application. It is in charge of sending
    messages to the server.

    Attributes:
        host (str):
            The hostname or ip address of the server
        port (int):
            The port of the server
        username (str):
            The client's username
    """

    def __init__(self, host="localhost", port=5555, username="User"):
        """
        Initializes a new client

        Parameters:
            host (str):
                The hostname or ip address of the server
            port (int):
                The port of the server
            username (str):
                The client's username
        """
        # Server host and port
        self.host = host
        self.port = port

        # Client username
        self.username = username

        # Server socket
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.settimeout(None)

        # Client state
        self.running = False
        self.receivingFromServer = False

    def receiveFromServer(self):
        """Receives an object from the server"""
        try:
            data = self.server.recv(4096)
        except BlockingIOError:
            # No more data from server
            pass
        else:
            if not data:
                # Server disconnected
                print("Server disconnected")
                self.running = False
                self.receivingFromServer = False

                # Post Pygame event
                if pygame.get_init():
                    pygame.event.post(
                        pygame.event.Event(
                            CLIENT_DISCONNECTED_EVENT,
                        )
                    )
            else:
                # Message received
                obj = pickle.loads(data)
                print(f"Received Object: {obj}")

                # Post Pygame event
                if pygame.get_init():
                    pygame.event.post(
                        pygame.event.Event(
                            CLIENT_MESSAGE_RECEIVED_EVENT,
                            sender=self.server,
                            message=obj,
                        )
                    )

    def sendToServer(self, obj):
        """
        Sends an object to the server

        Parameters:
            obj (Object):
                The object to send to the server
        """
        print(f"Sending Object: {obj}")
        obj.clientPort = self.server.getsockname()[1]
        data = pickle.dumps(obj)
        try:
            self.server.sendall(data)
        except (BrokenPipeError, ConnectionAbortedError, OSError):
            print(f"Failed to send to {self.server}")

    def start(self):
        """Starts the client"""
        try:
            self.server.connect((self.host, self.port))
        except OSError:
            print(f"Could not connect to server at {self.host}:{self.port}")
        else:
            print(f"Connected to server at {self.host}:{self.port}")
            self.running = True

            # Post Pygame event
            if pygame.get_init():
                pygame.event.post(
                    pygame.event.Event(
                        CLIENT_CONNECTED_EVENT,
                    )
                )

            self.receivingFromServer = True

            self.run()

    def stop(self):
        """Stops the client"""
        print("Stopping client")
        self.running = False

        self.receivingFromServer = False

        try:
            self.server.shutdown(socket.SHUT_RDWR)
        except OSError:
            # Server already shut down socket
            pass
        self.server.close()

    def run(self):
        """Runs the client"""
        while self.running:
            if self.receivingFromServer:
                self.receiveFromServer()
