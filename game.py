from enum import Enum
import pygame

from board import Board
from renderer import Renderer
from constants import *

class Game:
    '''
    Initialize board, runs TikTakToe mainloop.
    '''
    class GameState(Enum):
        Init: int = 0
        Running: int = 1
        Winner_X: int = 2
        Winner_0: int = 3
        Draw: int = 4

    def __init__(self, screen: pygame.surface.Surface = None, board: Board = None, renderer: Renderer = None):
        self.screen = screen or pygame.display.set_mode(WINDOW_SIZE)
        self.board = board or Board()
        self.renderer = renderer or Renderer(screen, "white")
        self.clock = pygame.time.Clock()
        self.state = Game.GameState.Init
        self.result_font = pygame.font.SysFont("Times New Roman", 40)

    def run(self):
        '''
        Game mainloop.
        '''
        self.state = Game.GameState.Running
        while True:
            match self.handle_events():
                case 0:
                    pass
                case 1:
                    return 1
                case 2:
                    return 2

            self.render()
            self.state = self.check_win_draw() or self.state

            self.clock.tick(10)

    def handle_events(self) -> int:
        '''
        Handles events.

        Returns 0 if game continues as normal.
        Returns 1 if Quit event is triggered.
        Returns 2 if game needs restart.
        '''
        while (event := pygame.event.poll()):
            # close button
            if event.type == pygame.QUIT:
                return 1
            # Escape key
            if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_ESCAPE):
                return 1
            # is game running ?
            if self.state == Game.GameState.Running:
                # left click
                if (event.type == pygame.MOUSEBUTTONUP) and (event.button == 1):
                    x, y = event.pos
                    i, j = x // CELL_SIZE, y // CELL_SIZE
                    self.board.turn(i, j)
            if self.state in (Game.GameState.Winner_0, Game.GameState.Winner_X, Game.GameState.Draw):
                if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_SPACE):
                    return 2
        return 0

    def render(self) -> None:
        '''
        Renders the game mainloop.
        '''
        self.screen.fill((0, 0, 0))
        match self.state:
            case Game.GameState.Running:
                self.renderer.draw_board(self.board)
            case Game.GameState.Draw:
                self.renderer.draw_text("Game is draw.", self.result_font)
            case Game.GameState.Winner_0:
                self.renderer.draw_text("Winner:\nO", self.result_font)
            case Game.GameState.Winner_X:
                self.renderer.draw_text("Winner:\nX", self.result_font)

        pygame.display.flip()

    def check_win_draw(self):
        '''
        Returns the state of the game in case of a draw or a win
        Else returns None
        '''
        if self.board.get_winner() == 'X':
            return Game.GameState.Winner_X
        elif self.board.get_winner() == '0':
            return Game.GameState.Winner_0
        elif self.board.is_draw():
            return Game.GameState.Draw
        return