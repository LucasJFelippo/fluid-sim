import math

class Pos():
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

class Vel():
    def __init__(self, abs, angle) -> None:
        self.abs = abs
        self.angle = math.radians(angle)
        self.x = self.abs * math.cos(self.angle)
        self.y = self.abs * math.sin(self.angle)