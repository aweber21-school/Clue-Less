from .Client import Client
from .Server import Server


class Network:
    def __init__(self):
        self.network = None

    def send(self, text):
        if self.network:
            self.network.send_text(text)

    def startClient(self, username='User', host='localhost', port=5555):
        # Just in case a network already exists
        self.stop()

        self.network = Client(username, host, port)
        self.network.start()

    def startServer(self, host='localhost', port=5555):
        # Just in case a network already exists
        self.stop()

        self.network = Server(host, port)
        self.network.start()

    def stop(self):
        if self.network:
            self.network.stop()
            self.network = None
