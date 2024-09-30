from typing import Callable
import pygame
import utils
from button import Button
from constants import *


class Menu():
    '''
    Game main menu.
    '''

    def __init__(self, name: str, size: tuple[int, int], font: pygame.font.Font = None):
        self.screen = pygame.display.set_mode(size)
        self.clock = pygame.time.Clock()
        self.font = font or pygame.font.SysFont("Times New Roman", 26)
        self.buttons = []
        self._sel = 0

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

        :param text: button text
        :param bind: callback function
        :param color: color for button text
        :param background: background for button
        :param mouseover_color: color for button text on mouseover
        :param mouseover_background: background for button on mouseover
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
                self._sel = i
            if self._sel == i:
                surface = button['output']['mouseover']
            else:
                surface = button['output']['default']
            self.screen.blit(surface, (x, y))
            y += height

        pygame.display.flip()

    def run(self):
        '''
        Runs menu mainloop.
        '''
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
                # go to previous menu
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return
                    # next button
                    elif event.key == pygame.K_UP:
                        self._sel = (self._sel - 1 + len(self.buttons)) % len(self.buttons)
                    # previous button
                    elif event.key == pygame.K_DOWN:
                        self._sel = (self._sel + 1) % len(self.buttons)
                    # press button
                    elif event.key == pygame.K_RETURN:
                        try:
                            self.buttons[self._sel]['binds'][1]()
                        except KeyError:
                            pass

                self.display()
            self.clock.tick(10)
