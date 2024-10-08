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


def create_theme() -> pygame_menu.themes.Theme:
    '''
    Creates theme for menus.

    :return: theme for pygame_menu.menu.Menu
    '''
    theme = pygame_menu.Theme(
        background_color=(40, 41, 35),
        cursor_color=(255, 255, 255),
        cursor_selection_color=(80, 80, 80, 120),
        scrollbar_color=(39, 41, 42),
        scrollbar_slider_color=(65, 66, 67),
        scrollbar_slider_hover_color=(90, 89, 88),
        selection_color=(255, 255, 255),
        title_background_color=(47, 48, 51),
        title_font_color=(215, 215, 215),
        widget_font_color=(200, 200, 200),

        title=False,
        widget_font_size=26,
    )

    return theme


def main():
    pygame.init()

    surface = pygame.display.set_mode(WINDOW_SIZE)

    theme = create_theme()

    # mode menu
    mode_menu = pygame_menu.Menu(
        "Mode menu",
        *WINDOW_SIZE,
        theme=theme,
    )

    mode_menu.add.button(
        "2 local players",
        Game().run,
        surface=surface,
        accept_kwargs=True,
    )

    mode_menu.add.button("Back", pygame_menu.events.BACK)

    # main menu
    main_menu = pygame_menu.Menu(
        "Main menu",
        *WINDOW_SIZE,
        theme=theme,
    )
    main_menu.add.button("Select mode", mode_menu)
    main_menu.add.button("Exit", pygame_menu.events.EXIT)

    main_menu.mainloop(surface)
    pygame.quit()


if __name__ == '__main__':
    main()
