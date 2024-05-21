import time, os

from src.simulation.simulator import Simulator

from src.event import BaseEvent
from src.in_out.events import Graphic_events
from src.physic.events import Physic_events

def start() -> None:
    sim = Simulator()

    while True:
        # handle all menu buffer events
        if not sim.menu_buffer.empty():
            event = sim.menu_buffer.get(block = False)
            if event.type == Graphic_events.WINDOWCLOSED:
                os._exit(0) # programming war crimes being commited TODO: fix this
            if event.type == Graphic_events.MENUVALUECHANGE:
                sim.arrange_particles(event.dict["number of particles"],
                                      event.dict["particle radius"],
                                      event.dict["particle spacing"])
            elif event.type == Graphic_events.SIMSTART:
                event = BaseEvent()
                event.type = Physic_events.SIMSTART
                sim.send_event(sim.physic_command_buffer, event)

        time.sleep(1 / 60)