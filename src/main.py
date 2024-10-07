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
from my_menu import Menu


def main():
    pygame.init()

    surface = pygame.display.set_mode(WINDOW_SIZE)

    main_menu = Menu("Main menu", *WINDOW_SIZE, surface)
    main_menu.run()

    pygame.quit()


if __name__ == '__main__':
    main()
