from enum import Enum
from abc import ABC, abstractmethod

from pygame import init
from pygame_widgets.slider import Slider
from pygame_widgets.button import Button

from src.objects.states import EngineStateTable
from config import NUMBER_OF_PARTICLES, PARTICLE, SCREEN_SIZE

from src.in_out.events import Graphic_events, BaseEvent

# the engines uses a state design pattern to control the behaviour of the engines in each state of the simulation
class ProtonState(ABC):
    @property
    def proton(self):
        return self._proton
    @proton.setter
    def proton(self, proton):
        self._proton = proton
    
    @abstractmethod
    def step(self) -> None:
        pass

class OffState(ProtonState):
    def step(self) -> None:
        pass

class MenuState(ProtonState):
    def step(self) -> None:
        self.proton.draw_particles()

        menu = self.proton.menu

        # handle the event of the start button
        if menu.start_sim:
            menu.off()
            self.proton.state = ProtonStateTable.RUNNING.value

            event = BaseEvent()
            event.type = Graphic_events.SIMSTART
            self.proton.send_menu_event(event)

            return

        # verify if there was a change on the value of each slider
        # TODO: make it recursively
        send_event = False
        number_of_particles_slider_value = menu.number_of_particles.getValue()
        if menu.number_of_particles_value != number_of_particles_slider_value:
            menu.number_of_particles_value = number_of_particles_slider_value
            send_event = True

        particle_radius_slider_value = menu.particle_radius.getValue()
        if menu.particle_radius_value != particle_radius_slider_value:
            menu.particle_radius_value = particle_radius_slider_value
            send_event = True

        particle_spacing_slider_value = menu.particle_spacing.getValue()
        if menu.particle_spacing_value != particle_spacing_slider_value:
            menu.particle_spacing_value = particle_spacing_slider_value
            send_event = True

        # if there was a change create an event and ask engine to send it to the simulator controller
        if send_event:
            event = BaseEvent()
            event.type = Graphic_events.MENUVALUECHANGE
            event.dict = {"number of particles": number_of_particles_slider_value,
                          "particle radius": particle_radius_slider_value,
                          "particle spacing": particle_spacing_slider_value}
            self.proton.send_menu_event(event)

        self.proton.draw_menu()

class RunningState(ProtonState):
    def step(self) -> None:
        self.proton.draw_particles()

class PausedState(ProtonState):
    def step(self) -> None:
        pass

class EndedState(ProtonState):
    def step(self) -> None:
        pass


# this dictionary create the instances of each state that the engine uses, to prevent the engine to have to create a new instance each time it changes it's internal state
class ProtonStateTable(Enum):
    OFF = OffState()
    MENU = MenuState()
    RUNNING = RunningState()
    PAUSED = PausedState()
    ENDED = EndedState()


class Menu:
    def __init__(self, screen, pg) -> None:
        self.screen = screen
        self.pg = pg

        # true if the start sim button is pressed
        self.start_sim = False

        # sets the x and y value of the menu, all elements inside it follow this two values
        self.x = SCREEN_SIZE['x'] - 150
        self.y = 30

        # sets the fonts that will be used by with pygame.Font.render()
        self.main_font = self.pg.font.SysFont("Arial", 12)

        self.slider_colour = (40, 40, 40)
        self.slider_handleColour = (0, 0, 0)
        self.text_colour = (170, 170, 170)

        # create each slider, and it's respective title text surfaces
        self.number_of_particles_value = NUMBER_OF_PARTICLES
        self.number_of_particles = Slider(
            win=self.screen,
            x=self.x,
            y=self.y + 20,
            width=100,
            height=10,
            min=1,
            max=3000,
            step=1,
            colour = self.slider_colour,
            handleColour = self.slider_handleColour,
            initial = NUMBER_OF_PARTICLES
        )
        self.number_of_particles_text_surface = self.main_font.render("Number of Particles", True, self.text_colour)

        self.particle_radius_value = PARTICLE['radius']
        self.particle_radius = Slider(self.screen, self.x, self.y + 60, 100, 10, min=0.1, max=10, step=0.1, colour = self.slider_colour, handleColour = self.slider_handleColour, initial = PARTICLE['radius'])
        self.particle_radius_text_surface = self.main_font.render("Particles Radius", True, self.text_colour)

        self.particle_spacing_value = PARTICLE['spacing']
        self.particle_spacing = Slider(self.screen, self.x, self.y + 100, 100, 10, min=0.1, max=5, step=0.1, colour = self.slider_colour, handleColour = self.slider_handleColour, initial = PARTICLE['spacing'])
        self.particle_spacing_text_surface = self.main_font.render("Particles Spacing", True, self.text_colour)

        self.start_button = Button(self.screen, self.x, self.y + 130, 105, 20, text = 'Start', font = self.main_font, textColour = self.text_colour, inactiveColour = self.slider_colour, hoverColour = self.slider_handleColour, pressedColour = (0, 200, 20), radius = 5, onClick = self.toggle_start
        )

    def on(self) -> None:
        # draw the background, set all sliders to show and blit all text surfaces to the frame
        background = self.pg.Rect(self.x - 15, self.y - 10, 140, 170)
        self.pg.draw.rect(self.screen, (55, 55, 55), background, border_radius = 5)
        # pygame widgets objects didn't have to be draw, they draw itselfs automaticly, show() and hide() toggle it's visibility
        self.number_of_particles.show()
        self.particle_radius.show()
        self.particle_spacing.show()
        self.screen.blit(self.number_of_particles_text_surface, (self.x - 5, self.y))
        self.screen.blit(self.particle_radius_text_surface, (self.x - 5, self.y + 40))
        self.screen.blit(self.particle_spacing_text_surface, (self.x - 5, self.y + 80))

    def off(self) -> None:
        # hide all sliders, this is called when Proton transition from Menu state to any other 
        self.number_of_particles.hide()
        self.particle_radius.hide()
        self.particle_spacing.hide()
        self.start_button.hide()

    def toggle_start(self) -> None:
        self.start_sim = not self.start_sim


class Proton:

    _state = ProtonStateTable.OFF.value

    def __init__(self, pg, screen, particles, command_buffer, menu_buffer) -> None:
        # the engine receave the pygame objects, signal buffer and particles from the simulation controller
        self.pg = pg
        self.screen = screen
        self.command_buffer = command_buffer
        self.menu_buffer = menu_buffer

        self.particles = particles

        self.on = True

        # set proton instance as the state.proton of each state object created on the state table
        for state in ProtonStateTable:
            state.value.proton = self

        # creates a menu to change the inicial simulation conditions, uses signal buffer to pass information for the simulation controller
        self.menu = Menu(self.screen, self.pg)

    @property
    def state(self) -> ProtonState:
        return self._state
    @state.setter
    def state(self, new_state) -> None:
        self._state = new_state

    def start(self) -> None:
        self.state = ProtonStateTable.MENU.value
    def stop(self) -> None:
        self.state = ProtonStateTable.OFF.value
    def terminate(self) -> None:
        self.stop()
        self.state = ProtonStateTable.ENDED.value
        self.on = False
        self.pg.display.quit()
        self.pg.quit()

        event = BaseEvent()
        event.type = Graphic_events.WINDOWCLOSED
        self.send_menu_event(event)

    @property
    def events(self) -> list:
        return self.pg.event.get()


    def step(self) -> None:
        # make the engine tick
        self._state.step()


    def send_menu_event(self, event) -> None:
        # called by Menu state
        self.menu_buffer.put(event)


    def draw_menu(self) -> None:
        self.menu.on()

    def undraw_menu(self) -> None:
        # pygame widget function different than pygame itself, objects created by pygame widget are automatic drawn on screen, so when transitioning from menu to other states, this function has to be call to undraw the sliders of the menu
        self.menu.off()

    def draw_particles(self) -> None:
        for particle in self.particles:
            self.pg.draw.circle(self.screen, particle.color, (particle.pos.x, particle.pos.y), particle.radius)