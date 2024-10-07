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
from game import Game


def main():
    pygame.init()

    game = Game(WINDOW_SIZE)
    game.run()

    pygame.quit()


if __name__ == '__main__':
    main()
