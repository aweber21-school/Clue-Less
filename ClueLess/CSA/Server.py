import pickle
import socket

import pygame

from ClueLess.Events import CLIENT_MESSAGE_RECEIVED_EVENT


class Server:
    """
    The Server for the Clue-Less application

    The Server class acts as the server in the Client-Server architecture
    implemented for the Clue-Less application. It is in charge of managing
    multiple client connections and sending messages to all clients.

    Attributes:
        username (str):
            The client's username
        host (str):
            The hostname or ip address of the server
        port (int):
            The port of the server
    """

    def __init__(self, host="localhost", port=5555, maxClients=2):
        """
        Initializes a new server

        Parameters:
            host (str):
                The hostname or ip address of the server
            port (int):
                The port of the server
            maxClients (int):
                The max number of clients that can connect to the server
        """
        # Server host and port
        self.host = host
        self.port = port

        # Server socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.settimeout(0.0)

        # Connected clients
        self.maxClients = maxClients
        self.clients = set()

        # Server state
        self.running = False
        self.acceptingNewClients = False
        self.receivingFromClients = False

    def acceptNewClients(self):
        """Accepts new clients trying to connect"""
        while True:
            try:
                connection, address = self.sock.accept()
            except BlockingIOError:
                # No more waiting clients
                break
            else:
                print(f"Client connected: {connection}, {address}")
                connection.settimeout(0.0)
                self.clients.add(connection)
                if len(self.clients) >= self.maxClients:
                    self.acceptingNewClients = False

    def receiveFromClients(self):
        """Receives an object from the clients"""
        for client in list(self.clients):
            try:
                data = client.recv(4096)
            except BlockingIOError:
                # No more data from client
                continue
            else:
                if not data:
                    # Client disconnected
                    print("Client disconnected")
                    client.shutdown(socket.SHUT_RDWR)
                    client.close()
                    self.clients.remove(client)
                else:
                    # Message received
                    obj = pickle.loads(data)
                    print(f"Received payload: {obj}")
                    if pygame.get_init():
                        pygame.event.post(
                            pygame.event.Event(
                                CLIENT_MESSAGE_RECEIVED_EVENT,
                                sender=client,
                                message=obj,
                            )
                        )

    def sendToClients(self, obj):
        """
        Sends an object to all of the server's clients

        Parameters:
            obj (Object):
                The object to send to clients
        """
        data = pickle.dumps(obj)
        for client in self.clients:
            try:
                client.sendall(data)
            except (BrokenPipeError, ConnectionAbortedError, OSError):
                print(f"Failed to send to {client}")

    def start(self):
        """Starts the server"""
        try:
            self.sock.bind((self.host, self.port))
        except OSError:
            print(f"Server already running on {self.host}:{self.port}")
        else:
            print(f"Starting server on {self.host}:{self.port}")
            self.running = True

            self.sock.listen(self.maxClients)
            self.acceptingNewClients = True
            self.receivingFromClients = True

            self.run()

    def stop(self):
        """Stops the server"""
        print("Stopping server")
        self.running = False

        self.acceptingNewClients = False
        self.receivingFromClients = False

        for client in list(self.clients):
            client.shutdown(socket.SHUT_RDWR)
            client.close()
            self.clients.remove(client)

        self.sock.shutdown(socket.SHUT_RDWR)
        self.sock.close()

    def run(self):
        """Runs the server"""
        while self.running:
            if self.acceptingNewClients:
                self.acceptNewClients()

            if self.receivingFromClients:
                self.receiveFromClients()
