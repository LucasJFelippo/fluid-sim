from enum import Enum, IntEnum, auto

class ObjectTypes(Enum):
    CIRCLE = auto()
    RECTANGLE = auto()

class Directions(IntEnum):
    RIGHT = 1
    LEFT = 2
    UP = 4
    DOWN = 8