import pygame as pg

from config import SCREEN_SIZE, BACKGROUND_COLOR, GRAPHICS_ENGINE
from src.graphics.options import OPTIONS as ENGINE_OPTIONS


def init_graphic_engine(particles) -> None:
    pg.init()
    screen = pg.display.set_mode((SCREEN_SIZE["x"], SCREEN_SIZE["y"]))

    Engine = ENGINE_OPTIONS[GRAPHICS_ENGINE]
    engine = Engine(pg, screen, particles)

    engine.start()