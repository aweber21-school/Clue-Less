from threading import Thread

from .Client import Client
from .Server import Server


class Network:
    """
    The Network Manager for Clue-Less application

    The Network class acts as the network manager for the Clue-Less
    application. This class is in charge of handling a server and/or client for
    communication.

    Attributes:
        server (ClueLess.CSA.Server):
            The server controlled by the network manager
        client (ClueLess.CSA.Client):
            The client controlled by the network manager
    """

    def __init__(self):
        """Initializes a new network"""
        self.server = None
        self.client = None

    def startServer(self, host="localhost", port=5555, maxClients=1):
        """
        Starts a new server

        Parameters:
            host (str):
                The hostname or ip address of the server
            port (int):
                The port of the server
            maxClients (int):
                The max number of clients that can connect to the server
        """
        self.server = Server(host, port, maxClients)
        Thread(target=self.server.start).start()

    def sendToClients(self, obj):
        """
        Sends an object to all of the server's clients

        Parameters:
            obj (Object):
                The object to send to clients
        """
        if self.server:
            self.server.sendToClients(obj)

    def stopServer(self):
        """Stops the server"""
        if self.server:
            self.server.stop()
            self.server = None

    def startClient(self, username="User", host="localhost", port=5555):
        """
        Starts a new client

        Parameters:
            username (str):
                The client's username
            host (str):
                The hostname or ip address of the server
            port (int):
                The port of the server
        """
        self.client = Client(username, host, port)
        Thread(target=self.client.start).start()

    def sendToServer(self, obj):
        """
        Sends an object to the server

        Parameters:
            obj (Object):
                The object to send to the server
        """
        if self.client:
            self.client.sendToServer(obj)

    def stopClient(self):
        """Stops the client"""
        if self.client:
            self.client.stop()
            self.client = None

    def start(self, username="User", host="localhost", port=5555, maxClients=1):
        """
        Starts a new server and a new client

        Parameters:
            username (str):
                The client's username
            host (str):
                The hostname or ip address of the server
            port (int):
                The port of the server
            maxClients (int):
                The max number of clients that can connect to the server
        """
        self.startServer(host, port, maxClients)
        self.startClient(username, host, port)

    def stop(self):
        """Stops the server and the client"""
        self.stopServer()
        self.stopClient()
