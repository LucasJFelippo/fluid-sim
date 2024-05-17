import time

from src.physic.atom import Atom

from config import PHYSIC_ENGINE
from src.physic.options import PHYSIC_ENGINE_CATALOG

from src.physic.events import Physic_events


def init_physic(particles, command_buffer) -> None:
    # init physic engine
    physic_engine = init_physic_engine(particles, command_buffer)

    # main loop
    while physic_engine.on:
        # handle all menu buffer events
        if not physic_engine.command_buffer.empty():
            event = physic_engine.command_buffer.get(block = False)
            if event.type == Physic_events.SIMSTART:
                physic_engine.start()

        # call the step on the engine, this indirect call the step of the state of the engine and make the engine tick
        physic_engine.step()


def init_physic_engine(particles, command_buffer):

    # get the name of the choosen physic engine from Config
    physic_engine_name = PHYSIC_ENGINE
    # get engine object from dictionary on options
    engine_object = PHYSIC_ENGINE_CATALOG[physic_engine_name]
    # return the instance of the engine
    return engine_object(particles, command_buffer)