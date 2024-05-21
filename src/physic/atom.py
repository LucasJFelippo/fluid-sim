import time, copy

from enum import Enum
from abc import ABC, abstractmethod

from pygame import Vector2
from config import GRAVITY, SCREEN_SIZE, COLLISIONDAMPING

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
        # calculate the delta time
        current_step_time = time.time()
        delta_time = current_step_time - self.atom.last_step_time

        self.atom.predict(delta_time)
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

        self.test_time = 0
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


    def predict(self, delta_time) -> None:
        last_state = copy.deepcopy(self.particles)
        for particle in self.particles:
            velocity = particle.vel

            velocity += self.gravity(delta_time)

            particle.move(delta_time)
            self.walls_collision(particle)


    def walls_collision(self, particle):
        # check if the particle is out of the screen
        if particle.pos.x - particle.radius < 0:
            particle.pos.x = particle.radius
            particle.vel.x *= -1 * COLLISIONDAMPING
        if particle.pos.x + particle.radius > SCREEN_SIZE['x']:
            particle.pos.x = SCREEN_SIZE['x'] - particle.radius
            particle.vel.x *= -1 * COLLISIONDAMPING
        if particle.pos.y - particle.radius < 0:
            particle.pos.y = particle.radius
            particle.vel.y *= -1 * COLLISIONDAMPING
        if particle.pos.y + particle.radius > SCREEN_SIZE['y']:
            particle.pos.y = SCREEN_SIZE['y'] - particle.radius
            particle.vel.y *= -1 * COLLISIONDAMPING

    # TODO: make the function to calculate the total velocity vector
    def gravity(self, delta_time) -> Vector2:
        return Vector2(0, GRAVITY * delta_time)