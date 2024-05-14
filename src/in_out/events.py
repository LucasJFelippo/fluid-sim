from abc import ABC, abstractmethod
from enum import Enum, auto

class Graphic_events(Enum):
    BASEVALUECHANGE = 0


class BaseEvent(ABC):
    @property
    def type(self):
        return self._type
    @type.setter
    def type(self, type):
        self._type = type
