import sys
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
    sys.exit(0)

from mainmenu import MainMenu
import config


def main():
    pygame.init()

    pygame.display.set_caption("TicTacToe by n1tr0xs")

    main_menu = MainMenu(
        'Main Menu',
        *config.MENU_WINDOW_SIZE,
        theme=config.menu_theme,
    )
    main_menu.run()

    pygame.quit()


if __name__ == '__main__':
    main()
