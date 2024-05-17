from enum import Enum
from abc import ABC, abstractmethod

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
        print("Loop")

class RunningState(AtomState):
    def step(self) -> None:
        pass

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
    
    def __init__(self, particles) -> None:
        self.particles = particles

        self.on = True


    @property
    def state(self) -> AtomState:
        return self._state
    @state.setter
    def state(self, new_state) -> None:
        self._state = new_state

    def start(self) -> None:
        self.state = AtomStateTable.RUNNING.value
    def stop(self) -> None:
        self.state = AtomStateTable.OFF.value
    def terminate(self) -> None:
        self.stop()
        self.state = AtomStateTable.ENDED.value
        self.on = False


    def step(self) -> None:
        # make the engine tick
        self._state.step()