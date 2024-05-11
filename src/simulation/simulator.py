from random import randint
from threading import Thread

from src.simulation.particle import Particle
from config import NUMBER_OF_PARTICLES, SCREEN_SIZE, GRAPHICS_ENGINE
from src.graphics.options import OPTIONS as GRAPHICS_OPTIONS

from src.graphics.core import init_graphic_engine

class Simulator:
    def __init__(self) -> None:
        self.particles = []

        for i in range(NUMBER_OF_PARTICLES):
            self.particles.append(Particle(randint(1, SCREEN_SIZE['x']), randint(1, SCREEN_SIZE['y'])))
        print(self.particles[10].pos.x)

        self.graphics_model = GRAPHICS_OPTIONS[GRAPHICS_ENGINE]
        self.graphics_thread = Thread(target=init_graphic_engine, args=[self.particles])

        self.graphics_thread.start()