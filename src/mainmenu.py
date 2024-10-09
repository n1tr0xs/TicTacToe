import pygame_menu
from menu import Menu
from modemenu import ModeMenu


class MainMenu(Menu):
    def __init__(self, title, width, height, theme):
        super().__init__(title, width, height, theme)
        self._menu.add.button('Select mode', self._mode_menu)
        self._menu.add.button('Exit', pygame_menu.events.EXIT)

    def _mode_menu(self):
        '''
        Runs ModeMenu.
        '''
        ModeMenu('Mode menu', self._width, self._height, self._theme).run()
        self.set_mode()
