from collections import defaultdict
from typing import Callable
import pygame
from constants import *


class Menu():
    '''
    Game main menu.
    '''

    def __init__(self, size: tuple[int, int], font: pygame.font.Font = None):
        self.screen = pygame.display.set_mode(size)
        self.clock = pygame.time.Clock()
        self.font = font or pygame.font.SysFont("Times New Roman", 26)
        self.buttons = []

    def add_button(
        self,
        text: str,
        onclick: Callable,
        font: pygame.font.Font = None,
        color: Colorable = "white",
        background: Colorable = None,
        mouseover_color: Colorable = "green",
        mouseover_background: Colorable = None,
    ) -> None:
        '''
        Adds menu button.

        text - button text
        bind - callback function
        color - color for button text
        background - background for button
        mouseover_color - color for button text on mouseover
        mouseover_background - background for button on mouseover
        '''
        self.buttons.append({
            'output': {
                'default': self.font.render(text, True, color, background),
                'mouseover': self.font.render(text, True, mouseover_color, mouseover_background),
            },
            'binds': {
                1: onclick,
            },
            'rect': pygame.Rect((0, 0), (0, 0)),
        })

    def remove_button(self, text: str) -> dict:
        '''
        Removes button from menu.

        text - button text

        Returns removed button as dict: {'output': pygame.surface.Surface, 'bind': Callable}
        '''
        return self.buttons.pop(text)

    def display(self):
        '''
        Displays menu.
        Updates self.rect corresponding to drawn buttons.
        '''
        self.screen.fill((0, 0, 0))
        screen_width, screen_height = self.screen.get_size()
        center_x, center_y = screen_width // 2, screen_height // 2
        total_height = 0
        for button in self.buttons:
            total_height += button['output']['default'].get_size()[1]

        y = center_y - total_height // 2
        center_x = screen_width // 2
        for i, button in enumerate(self.buttons):
            width, height = button['output']['default'].get_size()
            x = center_x - width // 2
            rect = pygame.Rect((x, y), (width, height))
            button['rect'] = rect
            if rect.collidepoint(pygame.mouse.get_pos()):
                surface = button['output']['mouseover']
            else:
                surface = button['output']['default']
            self.screen.blit(surface, (x, y))
            y += height

        pygame.display.flip()

    def run(self):
        while True:
            while (event := pygame.event.poll()):
                if event.type == pygame.QUIT:
                    utils.exit()
                if event.type == pygame.MOUSEBUTTONUP:
                    for i, button in enumerate(self.buttons):
                        if button['rect'].collidepoint(pygame.mouse.get_pos()):
                            try:
                                button['binds'][event.button]()
                            except KeyError:
                                pass
                self.display()
            self.clock.tick(10)
