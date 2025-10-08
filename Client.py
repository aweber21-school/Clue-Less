import socket
import threading
import time


class Client:
    def __init__(self, host='localhost', port=5555):
        # Server host and port to connect to
        self.host = host
        self.port = port

        # Run status and server socket
        self.running = False
        self.server = None

    def serverListener(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
                s.connect((self.host, self.port))
                s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, True)
                s.settimeout(1)
            except ConnectionRefusedError:
                print(
                    'Could not connect to ' + self.host + ':' + str(self.port)
                )
                self.running = False

            print('Connected to server:', s)
            self.server = s
            while self.running:
                try:
                    # # Receive data from server
                    # data = self.server.recv(4096)
                    pass
                except KeyboardInterrupt:
                    self.running = False
                time.sleep(0.05)

    def run(self):
        print('Starting Client')
        self.running = True

        print('Starting Server Listener')
        threading.Thread(target=self.serverListener).start()

        # Game Loop
        while self.running:
            try:
                time.sleep(0.05)
                # # Send move to server
                # self.server.sendall(data)
            except KeyboardInterrupt:
                self.running = False
        print('\nClient Stopped')


if __name__ == '__main__':
    # Get Server host to connect to
    host = input('Enter host (default = localhost): ').strip()
    if len(host) == 0:
        host = 'localhost'

    # Get Server port to connect to
    port = input('Enter port number (default = 5555): ').strip()
    if len(port) == 0:
        port = 5555
    else:
        port = int(port)

    # Create and run a new Client
    Client(host, port).run()
