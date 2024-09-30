import sys

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

    menu = Menu(WINDOW_SIZE)
    menu.add_button('Start game', run_game)
    menu.add_button('Exit', utils.exit)
    menu.run()

    pygame.quit()


if __name__ == '__main__':
    main()
