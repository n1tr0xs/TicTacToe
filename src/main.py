try:
    import pygame
    import pygame_menu
except ImportError:
    print('''
Some required Python modules are not installed:
    - pygame
    - pygame_menu
You can use `pip install -r requirements.txt` to install all required modules.
''')
    exit()

from constants import *
from game import Game


def start_game(surface: pygame.surface.Surface):
    game = Game()
    game.run(surface)


def main():
    pygame.init()
    surface = pygame.display.set_mode(WINDOW_SIZE)

    main_menu = pygame_menu.Menu("Main menu", *WINDOW_SIZE)
    main_menu.add.button(
        "Start game",
        start_game,
        surface=surface,
        accept_kwargs=True,
    )
    main_menu.add.button("Exit", pygame_menu.events.EXIT)

    main_menu.mainloop(surface)
    pygame.quit()


if __name__ == '__main__':
    main()
