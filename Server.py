import socket
import threading
import time


class Server:
    def __init__(self, host='localhost', port=5555, maxClients=6):
        # Server host and port
        self.host = host
        self.port = port

        # Connected clients
        self.maxClients = maxClients
        self.clients = []

        # Run status and thread count
        self.running = False
        self.numThreads = 0

    def clientListener(self, client):
        self.numThreads += 1

        client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        client.settimeout(1)

        while self.running:
            try:
                # # Receive data from client
                # data = client.recv(4096)
                pass
            except socket.timeout:
                pass
            time.sleep(0.05)

        self.numThreads -= 1

    def connectionListener(self):
        self.numThreads += 1

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                # Bind and listen
                s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
                s.bind((self.host, self.port))
                s.settimeout(1)
                s.listen()
            except OSError:
                print(
                    'Server already running on '
                    + self.host
                    + ':'
                    + str(self.port)
                )
                self.running = False

            while self.running:
                try:
                    # Accept a new connection
                    conn, addr = s.accept()
                    print('New Connection:', conn, addr)

                    # Allow up to 6 clients at a time
                    if len(self.clients) < self.maxClients:
                        self.clients.append(conn)
                        threading.Thread(
                            target=self.clientListener(conn), args=(conn,)
                        ).start()
                except socket.timeout:
                    pass
                time.sleep(0.05)

        self.numThreads -= 1

    def killServer(self):
        print('\nKilling Server')
        self.running = False
        while self.numThreads:
            time.sleep(0.05)

    def run(self):
        print('Starting Server')
        self.running = True

        print('Starting Connection Listener')
        threading.Thread(target=self.connectionListener).start()

        while self.running:
            try:
                time.sleep(0.05)
                # # Send game state to clients
                # for client in self.clients:
                #     try:
                #         client.sendall(data)
                #     except OSError:
                #         # Connection lost to client
                #         pass
            except KeyboardInterrupt:
                self.killServer()
            time.sleep(0.05)
        print('Server Killed')


if __name__ == '__main__':
    # Get Server host
    host = input('Enter host (default = localhost): ').strip()
    if len(host) == 0:
        host = 'localhost'

    # Get Server port
    port = input('Enter port number (default = 5555): ').strip()
    if len(port) == 0:
        port = 5555
    else:
        port = int(port)

    # Create and run a new Server
    Server(host, port, 6).run()
