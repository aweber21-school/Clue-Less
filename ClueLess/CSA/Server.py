# Server.py
import json
import socket
import pygame

from ClueLess.Events import CLIENT_MESSAGE_RECEIVED_EVENT


class Server:
    def __init__(self, host='localhost', port=5555, maxClients=2):
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
        while True:
            try:
                connection, address = self.sock.accept()
            except BlockingIOError:
                # No more waiting clients
                break
            else:
                print(f'Client connected: {connection}, {address}')
                connection.settimeout(0.0)
                self.clients.add(connection)
                if len(self.clients) >= self.maxClients:
                    self.acceptingNewClients = False

    def receiveFromClients(self):
        for client in list(self.clients):
            try:
                data = client.recv(4096)
            except BlockingIOError:
                # No more data from client
                continue
            else:
                if not data:
                    # Client disconnected
                    print('Client disconnected')
                    client.shutdown(socket.SHUT_RDWR)
                    client.close()
                    self.clients.remove(client)
                else:
                    # Message received
                    obj = json.loads(data.decode('utf-8'))
                    print(f'Received payload: {obj}')
                    if pygame.get_init():
                        pygame.event.post(
                            pygame.event.Event(
                                CLIENT_MESSAGE_RECEIVED_EVENT, sender=client, message=obj
                            )
                        )

    def sendToClients(self, obj):
        data = json.dumps(obj).encode('utf-8')
        for client in self.clients:
            try:
                client.sendall(data)
            except (BrokenPipeError, ConnectionAbortedError, OSError):
                print(f'Failed to send to {client}')

    def start(self):
        try:
            self.sock.bind((self.host, self.port))
        except OSError:
            print(f'Server already running on {self.host}:{self.port}')
        else:
            self.sock.listen(self.maxClients)
            print(f'Starting server on {self.host}:{self.port}')

            self.running = True
            self.acceptingNewClients = True
            self.receivingFromClients = True

            self.run()

    def stop(self):
        print('Stopping server')

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
        while self.running:
            if self.acceptingNewClients:
                self.acceptNewClients()

            if self.receivingFromClients:
                self.receiveFromClients()
