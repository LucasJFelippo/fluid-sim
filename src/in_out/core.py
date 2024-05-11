import pygame as pg
import time

from config import FRAME_RATE, SCREEN_SIZE, BACKGROUND_COLOR, GRAPHIC_ENGINE
from src.objects.states import EngineStateTable
from src.in_out.options import GRAPHIC_ENGINE_CATALOG
from src.in_out.out.proton import Proton


def init_in_out(particles, input_buffer, graphic_engine_signal_buffer) -> None:
    # setup pygame for graphic and mouse/keyboard input
    pg.init()
    
    # init out: graphic engine
    graphic_engine = init_graphic_engine(particles, graphic_engine_signal_buffer)

    # TODO: init the input handler

    # main loop
    graphic_engine.start()
    while graphic_engine.state != EngineStateTable.OFF and graphic_engine.state != EngineStateTable.ENDED:
        for event in graphic_engine.events:
            if event.type == graphic_engine.pg.QUIT:
                graphic_engine.terminate()

        graphic_engine.draw_frame()


        time.sleep(1 / FRAME_RATE)



def init_graphic_engine(particles, signal_buffer) -> Proton:
    # set the window screen
    screen = pg.display.set_mode((SCREEN_SIZE["x"], SCREEN_SIZE["y"]))

    # get the name of the choosen graphic engine from Config
    graphic_engine_name = GRAPHIC_ENGINE
    # get engine object from dictionary on options
    engine_object = GRAPHIC_ENGINE_CATALOG[graphic_engine_name]
    # return the instance of the engine
    return engine_object(pg, screen, particles, signal_buffer)
