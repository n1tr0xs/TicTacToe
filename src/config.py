import pygame_menu


MENU_WINDOW_SIZE = (360, 360)
GAME_WINDOW_SIZE = (240, 240)
CELLS = 3
FPS = 10

menu_theme = pygame_menu.Theme(
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
    widget_font_size=20,
)
