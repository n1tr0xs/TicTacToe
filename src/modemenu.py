from menu import Menu
from gamewtolocalplayers import GameTwoLocalPlayers
import config


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
