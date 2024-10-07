import pygame


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
        title_font: pygame.font.Font = None,
        widget_font: pygame.font.Font = None,
    ):
        self._surface = surface
        self._title = title
        self._title_font = title_font or pygame.font.SysFont(
            "Times New Roman", 40)
        self._widget_font = widget_font or pygame.font.SysFont(
            "Times New Roman", 20)
        self._width = width
        self._height = height

    def run(self, fps_limit: int = 10):
        while True:
            while (event := pygame.event.poll()):
                self.draw(self._surface)
            self._clock.Tick(fps_limit)

    def draw(self):
        print(f'Drawing Menu {self._title}')

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

    ''' Getters '''

    def get_size(self) -> tuple[int, int]:
        return (self._width, self._height)

    def get_width(self) -> int:
        return self._width

    def get_height(self) -> int:
        return self._height

    def get_surface(self) -> pygame.surface.Surface:
        return self._surface
