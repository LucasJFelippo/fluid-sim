import pygame as pg
import time, sys

import pygame_widgets as pg_widgets
from pygame_widgets.slider import Slider

from config import FRAME_RATE, SCREEN_SIZE, BACKGROUND_COLOR, GRAPHIC_ENGINE
from src.in_out.options import GRAPHIC_ENGINE_CATALOG


def init_in_out(particles, input_buffer, graphic_command_buffer, menu_buffer) -> None:
    # setup pygame for graphic and mouse/keyboard input
    pg.init()
    pg.font.init()

    # set the clock that will be used to control the frame rate
    clock = pg.time.Clock()

    # init out: graphic engine
    graphic_engine = init_graphic_engine(particles, graphic_command_buffer, menu_buffer)

    # main loop
    graphic_engine.start()
    while graphic_engine.on:
        for event in graphic_engine.events:
            if event.type == graphic_engine.pg.QUIT:
                graphic_engine.terminate()
                sys.exit()

        graphic_engine.screen.fill(BACKGROUND_COLOR)

        # call the step on the engine, this indirect call the step of the state of the engine and make the engine tick
        graphic_engine.step()

        pg_widgets.update(graphic_engine.events)
        graphic_engine.pg.display.flip()

        clock.tick(FRAME_RATE)


def init_graphic_engine(particles, command_buffer, menu_buffer):
    # set the window screen
    screen = pg.display.set_mode((SCREEN_SIZE["x"], SCREEN_SIZE["y"]))

    # get the name of the choosen graphic engine from Config
    graphic_engine_name = GRAPHIC_ENGINE
    # get engine object from dictionary on options
    engine_object = GRAPHIC_ENGINE_CATALOG[graphic_engine_name]
    # return the instance of the engine
    return engine_object(pg, screen, particles, command_buffer, menu_buffer)