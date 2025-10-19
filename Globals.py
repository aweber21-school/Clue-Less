# --- Constants --- #
class Constant:
    # WIDTH = 1280
    # HEIGHT = 720
    WIDTH = 640
    HEIGHT = 480


# --- Colors --- #
class Color:
    WHITE = (255, 255, 255)
    LIGHT_GRAY = (235, 235, 235)
    GRAY = (200, 200, 200)
    DARK_GRAY = (100, 100, 100)
    BLACK = (0, 0, 0)
    RED = (200, 40, 40)
    GREEN = (40, 160, 80)


# --- States --- #
class State:
    MAIN_MENU = 0
    SERVER_MENU = 1
    CLIENT_MENU = 2


# --- Role --- #
class Role:
    def __init__(self, name='', obj=None):
        self.name = name
        self.obj = obj
    def getName(self):
        return self.name
    def setName(self, name):
        self.name = name
    def getObj(self):
        return self.obj
    def setObj(self, obj):
        self.obj = obj
    def start(self):
        self.obj.start()
    def stop(self):
        self.obj.stop()
