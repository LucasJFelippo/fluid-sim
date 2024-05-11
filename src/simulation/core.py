import time
from threading import Thread

from src.simulation.simulator import Simulator

def start() -> None:
    sim = Simulator()

    inp = 1
    while inp != "e":
        sim.particles[4].pos.x += 100
        inp = input()