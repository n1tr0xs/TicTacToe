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
from renderer import Renderer
from game import Game

def main():
    screen = pygame.display.set_mode(WINDOW_SIZE)
    renderer = Renderer(screen, "white")

    while True:
        game = Game(screen=screen, renderer=renderer)
        match game.run():
            case 1:  # exit game
                return
            case 2:  # restart board
                continue


if __name__ == '__main__':
    pygame.init()
    main()
    pygame.quit()
