import pygame
import pygame_menu


class Menu:
    '''
    Menu handler class.

    :param title: Title of the Menu
    :param width: Width in px of the Menu
    :param height: Height in px of the Menu
    :param theme: pygame_menu Theme for Menu
    '''

    def __init__(
        self,
        title: str = '',
        width: int = 0,
        height: int = 0,
        theme: pygame_menu.themes.Theme = None
    ) -> None:
        self._width = width
        self._height = height
        self._theme = theme

        self._screen = self.set_mode()
        self._menu = pygame_menu.Menu(title, width, height, theme=theme)

    def run(self) -> None:
        '''
        Wrapper for pygame_menu.Menu.mainloop.
        '''
        self._menu.mainloop(self._screen)

    def set_mode(self) -> pygame.surface.Surface:
        '''
        Wrapper for pygame.display.set_mode.
        '''
        return pygame.display.set_mode((self._width, self._height))

    def add_button(self, *args, **kwargs) -> pygame_menu.widgets.Button:
        '''
        End-to-end wrapper for menu.add.button
        '''
        return self._menu.add.button(*args, **kwargs)
