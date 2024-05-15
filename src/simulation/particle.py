from src.objects.attributes import Pos, Vel
from config import PARTICLE

class Particle:
    def __init__(self, x, y, radius) -> None:
        self.pos = Pos(x, y)
        self.vel = Vel(0, 0)

        self.radius = radius
        self.color = PARTICLE["color"]