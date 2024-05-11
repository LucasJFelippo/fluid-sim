import time, sys

from src.objects.states import EngineStateTable

from config import SCREEN_SIZE, BACKGROUND_COLOR, FRAME_RATE
from src.objects.flags import ObjectTypes



class V1:

    _state = EngineStateTable.OFF

    def __init__(self, pg, screen, particles) -> None:
        self.pg = pg
        self.screen = screen

        self.particles = particles


    def start(self):
        self._state = EngineStateTable.RUNNING
        start_time = time.time()
        while self._state != EngineStateTable.ENDED and self._state != EngineStateTable.OFF:
            self.draw_frame()
            time.sleep(1 / FRAME_RATE)
            if time.time() - start_time > 3:
                break
        self.pg.display.quit()
        self.pg.quit()
        sys.exit()
            

    def draw_frame(self):
        for event in self.pg.event.get():
            if event.type == self.pg.QUIT:
                return 0

        self.screen.fill(BACKGROUND_COLOR)

        for particle in self.particles:
            self.pg.draw.circle(self.screen, particle.color, (particle.pos.x, particle.pos.x), particle.radius)

        self.pg.display.flip()

        return 1