from threading import Thread
from .Client import Client
from .Server import Server


class Network:
    def __init__(self):
        self.server = None
        self.client = None

    def startServer(self, host='localhost', port=5555, maxClients=2):
        # Just in case a server already exists
        # if self.server:
        #     self.server.stop()

        self.server = Server(host, port, maxClients)
        Thread(target=self.server.start).start()

    def sendToClients(self, obj):
        if self.server:
            self.server.sendToClients(obj)

    def stopServer(self):
        if self.server:
            self.server.stop()
            self.server = None

    def startClient(self, username='User', host='localhost', port=5555):
        # Just in case a client already exists
        # if self.client:
        #     self.client.stop()

        self.client = Client(username, host, port)
        Thread(target=self.client.start).start()

    def sendToServer(self, obj):
        if self.client:
            self.client.sendToServer(obj)

    def stopClient(self):
        if self.client:
            self.client.stop()
            self.client = None

    def stop(self):
        self.stopServer()
        self.stopClient()
