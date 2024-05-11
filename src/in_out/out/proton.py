import time, sys

from src.objects.states import EngineStateTable

from config import BACKGROUND_COLOR, FRAME_RATE



class Proton:

    _state = EngineStateTable.OFF

    def __init__(self, pg, screen, particles, signal_buffer) -> None:
        self.pg = pg
        self.screen = screen
        self.signal_buffer = signal_buffer

        self.particles = particles

    @property
    def state(self) -> EngineStateTable:
        return self._state
    @state.setter
    def state(self, new_state) -> EngineStateTable:
        self._state = new_state

    def start(self) -> None:
        self.state = EngineStateTable.RUNNING
    def stop(self) -> None:
        self.state = EngineStateTable.OFF
    def terminate(self) -> None:
        self.stop()
        self.state = EngineStateTable.ENDED
        self.pg.display.quit()
        self.pg.quit()
        sys.exit()

    @property
    def events(self) -> list:
        return self.pg.event.get()


    def draw_frame(self) -> None:
        self.screen.fill(BACKGROUND_COLOR)

        for particle in self.particles:
            self.pg.draw.circle(self.screen, particle.color, (particle.pos.x, particle.pos.x), particle.radius)

        self.pg.display.flip()