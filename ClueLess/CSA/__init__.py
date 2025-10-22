"""
Clue-Less Client-Server Architecture package

This package contains the Client-Server architecture for the Clue-Less game.

Modules:
    Client:
        The client for the network
    Server:
        The server for the network
"""

from .Network import Network
from .Client import Client
from .Server import Server

__all__ = ['Network', 'Client', 'Server']
