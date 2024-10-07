import pygame
from .actions import *
from ._types import *

__all__ = [
    'Widget',
]


class Widget:
    def __init__(
        self,
        title: str = '',
    ):
        self._title = title
        self._font = None
        self._rect = pygame.Rect(0, 0, 0, 0)
        self._selected = False

    def select(self):
        self._selected = True

    def is_selected(self):
        return self._selected

    def render_string(self):
        if self._font is None:
            return pygame.surface.Surface((0, 0))

        if self._selected:
            color = self._selected_color
            background = self._background
        else:
            color = self._color
            background = self._selected_background

        return self._font.render(self._title, True, color, background)

    '''
    Setters
    '''

    def set_title(self, title: str):
        self._title = title

    def set_font(
        self,
        font_name: str,
        font_size: int,
        color: Color = None,
        selected_color: Color = None,
        background: Color = None,
        selected_background: Color = None,
    ):
        self._font = pygame.font.SysFont(font_name, font_size)
        self._color = color
        self._selected_color = selected_color
        self._background = background
        self._selected_background = selected_background

    '''
    Getters
    '''

    def get_title(self) -> str:
        return self._title
