import pygame
from constants import *
from board import Board

class Renderer:
    '''
    Object for rendering game.
    '''

    def __init__(self, surface: pygame.surface.Surface, color: Colorable = "white"):
        '''
        Creates Rendere object.

        surface - pygame.surface.Surface
        color - pygame.Color or str or int or tuple[int, int, int, [int]]
        '''
        self.surface = surface
        self.color = pygame.Color(color)

    def draw_board(self, board: Board, color: Colorable = "white") -> None:
        '''
        Draws board on screen.

        board - Board object.
        color - pygame.Color or str or int or tuple[int, int, int, [int]]
        '''
        # draws vertical lines
        for i in range(1, CELLS):
            pygame.draw.line(
                self.surface, color or self.color,
                (CELL_SIZE * i, 0), (CELL_SIZE * i, CELL_SIZE * CELLS)
            )
        # draws horizontal lines
        for i in range(1, CELLS):
            pygame.draw.line(
                self.surface, color or self.color,
                (0, CELL_SIZE * i), (CELL_SIZE * CELLS, CELL_SIZE * i)
            )
        # draws signs on the board
        for i in range(board.size):
            for j in range(board.size):
                x = CELL_SIZE * i + CELL_SIZE // 2
                y = CELL_SIZE * j + CELL_SIZE // 2
                match board.get(i, j):
                    case 'X':
                        self.draw_X(x, y)
                    case '0':
                        self.draw_0((x, y))

    def draw_X(self, x: int, y: int, color: Colorable = None) -> None:
        '''
        Draws X with center in given coordinates.

        x - int
        y - int
        color - pygame.Color or str or int or tuple[int, int, int, [int]]
        '''
        coef = CELL_SIZE // 2 * .8
        pygame.draw.line(
            self.surface, color or self.color,
            (x - coef, y - coef),
            (x + coef, y + coef)
        )
        pygame.draw.line(
            self.surface, color or self.color,
            (x + coef, y - coef),
            (x - coef, y + coef)
        )

    def draw_0(self, center: tuple[int, int], color: Colorable = None) -> None:
        '''
        Draws 0 in given `center`.

        center  - center coordinates for the symbol
        color - pygame.Color or str or int or tuple[int, int, int, [int]]
        '''
        coef = CELL_SIZE // 2 * .85
        pygame.draw.circle(
            self.surface, color or self.color,
            center, coef, 1
        )
