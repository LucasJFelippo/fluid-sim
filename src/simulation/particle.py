from pygame import Vector2
from config import PARTICLE

class Particle:
    def __init__(self, x, y, radius) -> None:
        self.pos = Vector2(x, y)
        self.vel = Vector2(0, 0)

        self.radius = radius
        self.color = PARTICLE["color"]

    def move(self, delta_time):
        self.pos += self.vel * delta_time