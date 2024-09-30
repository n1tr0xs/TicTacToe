try:
    import pygame
except ImportError:
    print('''
Some required Python modules are not installed:
    - pygame
You can use `pip install -r requirements.txt` to install all required modules.
''')
    exit()

from constants import *
import utils
from menu import Menu
from game import Game


def run_game():
    game = Game(WINDOW_SIZE)
    game.run()


def main():
    pygame.init()

    main_menu = Menu('Main menu:', WINDOW_SIZE)
    mode_menu = Menu('Modes menu:', WINDOW_SIZE)

    # mode menu
    mode_menu.add_button('2 players on 1 PC', run_game)
    # mode_menu.add_button('Play with Bot', lambda: ...)
    # mode_menu.add_button('2 online players', lambda: ...)
    mode_menu.add_button('Back', main_menu.run)

    # main menu
    main_menu.add_button('Select mode', mode_menu.run)
    main_menu.add_button('Exit', utils.exit)
    main_menu.run()

    pygame.quit()


if __name__ == '__main__':
    main()
