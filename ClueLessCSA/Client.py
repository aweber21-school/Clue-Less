# Client.py
import socket
import threading
import select
import pygame as pg
import queue

NETWORK_EVENT = pg.USEREVENT + 1


class Client(threading.Thread):
    def __init__(
        self, username="User", host="localhost", port=5555, post_as_event=True
    ):
        super().__init__(daemon=True)
        self.username = username
        self.host = host
        self.port = port
        self.sock = None
        self.stop_event = threading.Event()
        self.post_as_event = post_as_event
        self.send_queue = queue.Queue()

    def stop(self):
        self.stop_event.set()
        try:
            if self.sock:
                self.sock.shutdown(socket.SHUT_RDWR)
                self.sock.close()
        except:
            pass

    def send_text(self, text):
        self.send_queue.put(text)

    def _push_to_gui(self, sender, text):
        if self.post_as_event and pg.get_init():
            pg.event.post(pg.event.Event(NETWORK_EVENT, payload=(sender, text)))

    def run(self):
        try:
            self.sock = socket.create_connection((self.host, self.port), timeout=5)
            self.sock.setblocking(False)
            self._push_to_gui("system", f"Connected to {self.host}:{self.port}")

            buffer = b""
            while not self.stop_event.is_set():
                # Outgoing
                try:
                    while True:
                        msg = self.send_queue.get_nowait()
                        wire = (msg.rstrip("\n") + "\n").encode("utf-8")
                        self.sock.sendall(wire)
                except queue.Empty:
                    pass

                # Incoming
                rlist, _, _ = select.select([self.sock], [], [], 0.05)
                if rlist:
                    chunk = self.sock.recv(4096)
                    if not chunk:
                        self._push_to_gui("system", "Server closed")
                        break
                    buffer += chunk
                    while b"\n" in buffer:
                        line, buffer = buffer.split(b"\n", 1)
                        text = line.decode("utf-8", errors="replace")
                        self._push_to_gui("server", text)
        except Exception as e:
            self._push_to_gui("system", f"Connection error: {e}")
        finally:
            if self.sock:
                self.sock.close()
            self._push_to_gui("system", "Disconnected")
