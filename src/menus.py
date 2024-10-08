import pygame
import pygame_menu
import config
from tictactoe import GameTwoLocalPlayers


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


class MainMenu(Menu):
    def __init__(self, title, width, height, theme):
        super().__init__(title, width, height, theme)
        self._menu.add.button('Select mode', self._mode_menu)
        self._menu.add.button('Exit', pygame_menu.events.EXIT)

    def _mode_menu(self):
        '''
        Calls Mode Menu.
        '''
        ModeMenu('Mode menu', self._width, self._height, self._theme).run()
        self.set_mode()


class ModeMenu(Menu):
    def __init__(self, title, width, height, theme):
        super().__init__(title, width, height, theme)
        self._menu.add.button('Player vs Player (local)',
                              self._two_local_players)
        self._menu.add.button('Back', self._menu.disable)

    def _two_local_players(self):
        game = GameTwoLocalPlayers(*config.GAME_WINDOW_SIZE, config.FPS)
        game.run()
        self._menu.disable()
