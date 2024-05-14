from enum import Enum, auto

class EngineStateTable(Enum):
    OFF = 0
    MENU = 2
    RUNNING = 4
    PAUSED = 8
    ENDED = 16