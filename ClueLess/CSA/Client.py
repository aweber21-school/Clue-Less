import json
import socket

import pygame

from ClueLess.Events import SERVER_MESSAGE_RECEIVED_EVENT


class Client:
    """
    The Client for the Clue-Less application

    The Client class acts as the client in the Client-Server architecture
    implemented for the Clue-Less application. It is in charge of sending
    messages to the server.

    Attributes:
        username (str):
            The client's username
        host (str):
            The hostname or ip address of the server
        port (int):
            The port of the server
    """
    def __init__(self, username="User", host="localhost", port=5555):
        """
        Initializes a new client

        Parameters:
            username (str):
                The client's username
            host (str):
                The hostname or ip address of the server
            port (int):
                The port of the server
        """
        # Client username
        self.username = username

        # Server host and port
        self.host = host
        self.port = port

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
            # No more data from client
            pass
        else:
            if not data:
                # Server disconnected
                print("Server disconnected")
                self.stop()
            else:
                # Message received
                obj = json.loads(data.decode("utf-8"))
                print(f"Received object: {obj}")
                if pygame.get_init():
                    pygame.event.post(
                        pygame.event.Event(
                            SERVER_MESSAGE_RECEIVED_EVENT,
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
        data = json.dumps(obj).encode("utf-8")
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
