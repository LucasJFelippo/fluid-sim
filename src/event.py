class BaseEvent:
    @property
    def type(self):
        return self._type
    @type.setter
    def type(self, type):
        self._type = type

    @property
    def dict(self):
        return self._dict
    @dict.setter
    def dict(self, dict):
        self._dict = dict