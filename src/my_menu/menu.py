import pygame
from .menubar import MenuBar
from .actions import *
from ._types import *

__all__ = [
    'Menu',

]


class Menu:
    '''
    Menu object.

    :param title: Title of the Menu
    :param width: Width of the Menu in px
    :param height: Height of the Menu in px

    :param surface: Pygame surface to draw the Menu
    :pararm title_font: Pygame font to print the Menu title. Default is SysFont("Times New Roman", 40)
    :pararm widget_font: Pygame font to print the Menu widgets. Default is SysFont("Times New Roman", 20)
    '''

    def __init__(
        self,
        title: str,
        width: int,
        height: int,
        surface: pygame.surface.Surface = None,
    ):
        self._surface = surface
        self._menu_bar = MenuBar(title)
        self.set_title_font()
        self.set_widget_font()        
        self._width = width
        self._height = height
        self._clock = pygame.time.Clock()

    def run(self, fps_limit: int = 10):
        while True:
            while (event := pygame.event.poll()):
                if event.type == pygame.QUIT:
                    exit()

                self.draw()
            self._clock.tick(fps_limit)

    def draw(self):
        self._surface.fill((0, 0, 0))
        menu_bar = self._menu_bar.render()

        self._surface.blit(menu_bar, (0, 0))

        pygame.display.flip()

    ''' Setters '''

    def set_size(self, width: int, height: int):
        self._width = width
        self._height = height

    def set_width(self, width: int):
        self._width = width

    def set_height(self, height: int):
        self._height = height

    def set_surface(self, surface: pygame.surface.Surface):
        self._surface = surface

    def set_title_font(
        self,
        font_name: str = 'Times New Roman',
        font_size: int = 40,
        color: Color = 'white',
        selected_color: Color = None,
        background: Color = None,
        selected_background: Color = None,
    ):
        self._menu_bar.set_font(font_name, font_size, color, selected_color, background, selected_background)

    def set_widget_font(
        self,
        font_name: str = 'Times New Roman',
        font_size: int = 20,
        color: Color = 'white',
        selected_color: Color = None,
        background: Color = None,
        selected_background: Color = None,
    ):
        self._widget_font = (font_name, font_size, color, selected_color, background, selected_background)

    ''' Getters '''

    def get_size(self) -> tuple[int, int]:
        return (self._width, self._height)

    def get_width(self) -> int:
        return self._width

    def get_height(self) -> int:
        return self._height

    def get_surface(self) -> pygame.surface.Surface:
        return self._surface
