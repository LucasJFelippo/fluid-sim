from enum import Enum, auto

class EngineStateTable(Enum):
    ENDED = 0
    OFF = 2
    RUNNING = 4
    PAUSED = 8