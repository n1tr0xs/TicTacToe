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
    while True:
        game = Game()
        match game.run():
            case 1:  # exit game
                return
            case 2:  # restart board
                continue


if __name__ == '__main__':
    pygame.init()
    main()
    pygame.quit()
