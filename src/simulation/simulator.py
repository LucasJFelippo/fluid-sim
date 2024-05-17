from threading import Thread
import queue
from random import randint
import math

from src.simulation.particle import Particle
from config import NUMBER_OF_PARTICLES, PARTICLE, PHYSIC_ENGINE, SCREEN_SIZE, GRAPHIC_ENGINE
from src.in_out.options import GRAPHIC_ENGINE_CATALOG

from src.in_out.core import init_in_out
from src.physic.core import init_physic

class Simulator:
    def __init__(self) -> None:
        # create the array that will contain all particles of simulation
        # this array is will be passed to both physics (read and write) and graphic (read only) thread
        self.particles = []

        # get the base values of mutable information of particles
        self.number_of_particles = NUMBER_OF_PARTICLES
        self.particles_radius = PARTICLE['radius']
        self.particles_spacing = PARTICLE['spacing']

        # populate the particles in a grid starting position
        self.arrange_particles(self.number_of_particles, self.particles_radius, self.particles_spacing)


        # create the queue that will be used as buffers to transmit information between the threads
        # input buffer: will be feed the inputs of the user inside graphic thread, where pygame stuff is, and will be read by the main thread
        self.input_buffer = queue.Queue() #TODO: implement the particles controlled by mouse
        # graphic command buffer and menu buffers: will be feed by the main thread, to transmit commands like close the window to the graphic thread controller, and tranmit information from the simulation menu and mouse from withing graphics engine
        self.graphic_command_buffer = queue.Queue() #TODO: unused
        self.menu_buffer = queue.Queue()
        # physic command buffer: will be feed by the main thread, to transmit commands like change state to the physic thread
        self.physic_command_buffer = queue.Queue()


        # register the name of the graphic engine being used, according to config
        self.graphic_engine_model = GRAPHIC_ENGINE
        # creating and starting the thread that handle the output (graphic engine) and input (mouse and keyboard)
        self.in_out_thread = Thread(target=init_in_out, args=[self.particles, self.input_buffer, self.graphic_command_buffer, self.menu_buffer])
        self.in_out_thread.start()

        # register the name of the physic engine being used, according to config
        self.physic_engine_model = PHYSIC_ENGINE
        # creating and starting the thread that calculate the particles movement (physic engine)
        self.physic_thread = Thread(target=init_physic, args=[self.particles, self.physic_command_buffer])
        self.physic_thread.start()


    def arrange_particles(self, number_of_particles, radius, spacing) -> None:
        # clear the current arrange of particles
        self.particles.clear()

        particles_per_row = math.floor(number_of_particles**0.5)
        particles_per_col = math.ceil(number_of_particles / particles_per_row)
        spacing = radius * 2 + spacing

        starting_x = SCREEN_SIZE['x'] / 2 - particles_per_row / 2 * spacing
        starting_y = SCREEN_SIZE['y'] / 2 - particles_per_col / 2 * spacing

        for i in range(number_of_particles):
            x = starting_x + i % particles_per_row * spacing
            y = starting_y + i // particles_per_row * spacing
            self.particles.append(Particle(x, y, radius))


    def send_event(self, buffer, event):
        buffer.put(event)