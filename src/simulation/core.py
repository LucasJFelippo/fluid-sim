import time

from src.simulation.simulator import Simulator
from src.in_out.events import Graphic_events

def start() -> None:
    sim = Simulator()

    while True:
        # handle all menu buffer events
        if not sim.menu_buffer.empty():
            event = sim.menu_buffer.get(block = False)
            if event.type == Graphic_events.MENUVALUECHANGE:
                sim.arrange_particles(event.dict["number of particles"],
                                      event.dict["particle radius"],
                                      event.dict["particle spacing"])


        time.sleep(1 / 60)