try:
    import pygame
except ImportError:
    print('''
Some required Python modules are not installed:
    - pygame
You can use `pip install -r requirements.txt` to install all required modules.
''')
    exit()

from game import Game


def main():
    game = Game()
    game.run()


if __name__ == '__main__':
    pygame.init()
    main()
    pygame.quit()
