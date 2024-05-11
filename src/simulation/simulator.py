from random import randint
from threading import Thread
import queue

from src.simulation.particle import Particle
from config import NUMBER_OF_PARTICLES, SCREEN_SIZE, GRAPHIC_ENGINE
from src.in_out.options import GRAPHIC_ENGINE_CATALOG

from src.in_out.core import init_in_out

class Simulator:
    def __init__(self) -> None:
        # create the array that will contain all particles of simulation
        # this array is will be passed to both physics (read and write) and graphic (read only) thread
        self.particles = []

        # temporary: populate the particles with random particles
        # TODO: make the logic of defaut particle spawn
        for i in range(NUMBER_OF_PARTICLES):
            self.particles.append(Particle(randint(1, SCREEN_SIZE['x']), randint(1, SCREEN_SIZE['y'])))


        # create the queue that will be used as buffers to transmit information between the in/out thread and the main thread
        # input buffer: will be feed the inputs of the user inside graphic thread, where pygame stuff is, and will be read by the main thread
        self.input_buffer = queue.Queue()
        # signal buffer: will be feed by the main thread, to transmit commands like close the window to the graphic thread controler
        self.graphic_engine_signal_buffer = queue.Queue()
        

        # register the name of the graphic engine being used, according to config
        self.graphic_engine_model = GRAPHIC_ENGINE

        # creating and starting the thread that handle the output (graphic engine) and input (mouse and keyboard)
        self.in_out_thread = Thread(target=init_in_out, args=[self.particles, self.input_buffer, self.graphic_engine_signal_buffer])
        self.in_out_thread.start()