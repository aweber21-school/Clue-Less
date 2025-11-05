# Clue-Less
The repository contains the game Clue-Less implemented by Team AREA for EN.605.601

## Usage
Open up a terminal and navigate to the local copy of this repository. Run the following command to run our Clue-Less application:

```Terminal
python App.py
```

## App
The App class serves as the top level class for our Clue-Less application. It contains the main Pygame game loop and maintains the application's Model-View-Controller Architecture (MVC). It also is in charge of facilitating the Client-Server Architecture (CSA).

## MVC Package
The Clue-Less MVC package contains the Model-View-Controller architecture for our Clue-Less game.

### Model
The Model class maintains the app state for our Clue-Less application. It acts as the Model in the Model-View-Controller (MVC) architecture.

## View
The View class serves as the GUI for our Clue-Less application. It acts as the View in the Model-View-Controller (MVC) architecture.

### Controller
The Controller class serves as the mediator for our Clue-Less Model and View. It acts as the Controller in the Model-View-Controller (MVC) architecture.

## CSA Package
The Clue-Less CSA package contains the Client-Server Architecture for our Clue-Less game.

### Network
The Network class acts as the network manager for the Clue-Less application. This class is in charge of handling a server and/or client for communication.

### Server
The Server class acts as the server in the Client-Server architecture implemented for the Clue-Less application. It is in charge of managing multiple client connections and sending messages to all clients.

### Client
The Client class acts as the client in the Client-Server architecture implemented for the Clue-Less application. It is in charge of sending messages to the server.
