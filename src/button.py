from collections import defaultdict
from typing import Callable
import pygame
from constants import *


class Button:
    '''
    Button object
    '''

    def __init__(
        self,
        text: str,
        onclick: Callable,
        font: pygame.font.Font = None,
        color: Colorable = "white",
        background: Colorable = None,
        mouseover_color: Colorable = "green",
        mouseover_background: Colorable = None,
    ):
        '''
        :param text: button text
        :param bind: callback function
        :param color: color for button text
        :param background: background for button
        :param mouseover_color: color for button text on mouseover
        :param mouseover_background: background for button on mouseover
        '''
        self.binds = {
            1: onclick,
        }
        font = font or pygame.font.SysFont("Times New Roman", 26)
        self.renders = {
            'default': font.render(
                text, True, color, background
            ),
            'mouseover': font.render(
                text, True, mouseover_color, mouseover_background
            ),
        }
        self.rect = pygame.Rect(0, 0, 0, 0)

    def is_selected(self) -> bool:
        '''
        Checks is button selected.

        :return: is button clicked
        '''
        return self.rect.collidepoint(pygame.mouse.get_pos())

    def draw(self, surface: pygame.surface.Surface, dest: tuple[int, int]) -> pygame.Rect:
        '''
        Draws button.
        Updates self.rect.

        :param dest: left top corner for button
        :return: area of affected pixels
        '''
        render = self.renders['default']
        size = render.get_size()
        self.rect = pygame.Rect(dest, size)
        if self.is_selected():
            render = self.renders['mouseover']
        return surface.blit(render, dest)
