from src.objects.attributes import Pos, Vel
from config import PARTICLE

class Particle:
    def __init__(self, x, y) -> None:
        self.pos = Pos(x, y)
        self.vel = Vel(0, 0)

        self.radius = PARTICLE["radius"]
        self.color = PARTICLE["color"]