import time

from enum import Enum
from abc import ABC, abstractmethod

from config import GRAVITY, VELOCITYWEIGHT

# the engines uses a state design pattern to control the behaviour of the engines in each state of the simulation
class AtomState(ABC):
    @property
    def atom(self):
        return self._atom
    @atom.setter
    def atom(self, atom):
        self._atom = atom
    
    @abstractmethod
    def step(self) -> None:
        pass

class OffState(AtomState):
    def step(self) -> None:
        pass

class RunningState(AtomState):
    def step(self) -> None:
        current_step_time = time.time()
        step_time_difference = current_step_time - self.atom.last_step_time
        if step_time_difference == 0:
            step_time_difference = 0.001
        step_per_second = 1 / step_time_difference
        self.atom.gravity(step_per_second)
        self.atom.last_step_time = current_step_time

class PausedState(AtomState):
    def step(self) -> None:
        pass

class EndedState(AtomState):
    def step(self) -> None:
        pass


# this dictionary create the instances of each state that the engine uses, to prevent the engine to have to create a new instance each time it changes it's internal state
class AtomStateTable(Enum):
    OFF = OffState()
    RUNNING = RunningState()
    PAUSED = PausedState()
    ENDED = EndedState()


class Atom:
    
    _state = AtomStateTable.OFF.value
    
    def __init__(self, particles, command_buffer) -> None:
        self.particles = particles

        self.command_buffer = command_buffer

        self.on = True

        self.velocity_weight = VELOCITYWEIGHT

        self.last_step_time = 0

        # set atom instance as the state.atom of each state object created on the state table
        for state in AtomStateTable:
            state.value.atom = self

    @property
    def state(self) -> AtomState:
        return self._state
    @state.setter
    def state(self, new_state) -> None:
        self._state = new_state

    def start(self) -> None:
        self.state = AtomStateTable.RUNNING.value
        self.last_step_time = time.time()
    def stop(self) -> None:
        self.state = AtomStateTable.OFF.value
    def terminate(self) -> None:
        self.stop()
        self.state = AtomStateTable.ENDED.value
        self.on = False


    def step(self) -> None:
        # make the engine tick
        self._state.step()


    # TODO: make the function to calculate the total velocity vector
    def gravity(self, time_difference) -> None:
        # TODO: make gravity change particle velocity
        for particle in self.particles:
            particle.pos.y += GRAVITY / time_difference * self.velocity_weight