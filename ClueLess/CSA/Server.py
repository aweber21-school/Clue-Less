# Server.py
import socket
import select
import threading
from collections import deque


class Server(threading.Thread):
    def __init__(self, host="localhost", port=5555):
        super().__init__(daemon=True)
        self.host = host
        self.port = port
        self.stop_event = threading.Event()
        self.sock = None
        self.clients = set()
        self.buffers = {}
        self.messages = deque(maxlen=100)  # log for GUI
        self.counts = {"RED": 0, "GREEN": 0}

    def log(self, msg):
        self.messages.append(msg)
        print(msg)

    def stop(self):
        self.stop_event.set()
        try:
            if self.sock:
                self.sock.shutdown(socket.SHUT_RDWR)
                self.sock.close()
        except:
            pass

    def broadcast_counts(self):
        """
        Broadcast current counts to all clients in the format:
        RED:<count>|GREEN:<count>
        """
        state = f"RED:{self.counts['RED']}|GREEN:{self.counts['GREEN']}\n".encode(
            "utf-8"
        )
        for c in list(self.clients):
            try:
                c.sendall(state)
            except:
                self.clients.discard(c)
                self.buffers.pop(c, None)
                try:
                    c.close()
                except:
                    pass

    def run(self):
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.sock.bind((self.host, self.port))
            self.sock.listen(5)
            self.sock.setblocking(False)
            self.log(f"Server listening on {self.host}:{self.port}")

            while not self.stop_event.is_set():
                rlist, _, _ = select.select(
                    [self.sock] + list(self.clients), [], [], 0.05
                )
                for s in rlist:
                    if s is self.sock:
                        conn, addr = self.sock.accept()
                        conn.setblocking(False)
                        self.clients.add(conn)
                        self.buffers[conn] = b""
                        self.log(f"Client connected: {addr}")
                        self.broadcast_counts()  # send current state to new client
                    else:
                        try:
                            data = s.recv(4096)
                            if not data:
                                self.clients.discard(s)
                                self.buffers.pop(s, None)
                                s.close()
                                self.log("Client disconnected")
                                continue

                            self.buffers[s] += data
                            while b"\n" in self.buffers[s]:
                                line, self.buffers[s] = self.buffers[s].split(b"\n", 1)
                                text = line.decode("utf-8", errors="replace")
                                # Expected format: USER|RED or USER|GREEN
                                parts = text.split("|")
                                if len(parts) == 2:
                                    user, color = parts
                                    color = color.strip().upper()
                                    if color in self.counts:
                                        self.counts[color] += 1
                                        self.log(
                                            f"{user} pressed {color} — totals {self.counts}"
                                        )
                                        self.broadcast_counts()
                                else:
                                    self.log(f"Bad message: {text}")
                        except Exception:
                            self.clients.discard(s)
                            self.buffers.pop(s, None)
                            try:
                                s.close()
                            except:
                                pass
        except OSError:
            self.stop()
        finally:
            for c in list(self.clients):
                c.close()
            if self.sock:
                self.sock.close()
            self.log("Server stopped")
