import time

from src.physic.atom import Atom

from config import PHYSIC_ENGINE
from src.physic.options import PHYSIC_ENGINE_CATALOG


def init_physic(particles):
    # init physic engine
    physic_engine = init_physic_engine(particles)

    # main loop
    while physic_engine.on:
        # call the step on the engine, this indirect call the step of the state of the engine and make the engine tick
        physic_engine.step()


def init_physic_engine(particles):

    # get the name of the choosen physic engine from Config
    physic_engine_name = PHYSIC_ENGINE
    # get engine object from dictionary on options
    engine_object = PHYSIC_ENGINE_CATALOG[physic_engine_name]
    # return the instance of the engine
    return engine_object(particles)