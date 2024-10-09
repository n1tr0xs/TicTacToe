import config
from menu import Menu
from gameplayerplayerlocal import GamePlayerPlayerLocal
from bot import GamePlayerBot


class ModeMenu(Menu):
    '''
    Mode select menu.
    Available modes:
        1. Player vs Player local
        2. Player vs Bot
    '''

    def __init__(self, title, width, height, theme):
        super().__init__(title, width, height, theme)
        self._menu.add.button('Player vs Player (local)', self._player_player_local)
        self._menu.add.button('Player vs Bot', self._player_bot)
        self._menu.add.button('Back', self._menu.disable)

    def _player_player_local(self) -> None:
        '''
        Runs Player vs Player (local) mode.
        '''
        GamePlayerPlayerLocal(*config.GAME_WINDOW_SIZE, config.FPS).run()
        self._menu.disable()

    def _player_bot(self) -> None:
        '''
        Runs SignMenu.
        '''
        SignMenu("Select your sign", self._width, self._height, self._theme).run()
        self.set_mode()


class SignMenu(Menu):
    '''
    Sign select menu for Player vs Bot mode.
    '''

    def __init__(self, title, width, height, theme):
        super().__init__(title, width, height, theme)
        self._menu.add.button('X', self._sign_X)
        self._menu.add.button('O', self._sign_O)
        self._menu.add.button('Back', self._menu.disable)

    def _sign_X(self) -> None:
        GamePlayerBot(*config.GAME_WINDOW_SIZE, config.FPS, 'X').run()

    def _sign_O(self) -> None:
        GamePlayerBot(*config.GAME_WINDOW_SIZE, config.FPS, 'O').run()
