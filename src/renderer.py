import pygame
from constants import *
from board import Board


class Renderer:
    '''
    Object for rendering game.
    '''

    def __init__(self, surface: pygame.surface.Surface, color: Colorable = None, font: pygame.font.Font = None):
        '''
        Creates Rendere object.

        surface - pygame.surface.Surface
        color - pygame.Color or str or int or tuple[int, int, int, [int]]
        '''
        self.surface = surface
        self.color = color or pygame.Color("white")
        self.font = font or pygame.font.SysFont("Times New Roman", 20)

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

    def draw_text(
        self,
        text: str,
        font: pygame.font.Font = None,
        color: Colorable = None,
        antialias: bool = True,
        background: Colorable = None,
        center: tuple[int, int] = None
    ) -> None:
        '''
        Draws multiline text.

        text - [multi]line text to draw
        font - font for drawing text
        color - foreground color
        antialias - antialiasing
        background - background color
        center - center coordinates of text
        '''
        font = font or self.font
        color = color or self.color
        x, y = center or map(lambda a: a // 2, self.surface.get_size())

        lines = text.split('\n')
        y -= sum(font.size(line)[1] for line in lines) // 2
        for line in lines:
            ren = font.render(
                line, antialias,
                color, background,
            )
            self.surface.blit(ren, (x - ren.get_size()[0] // 2, y))
            y += ren.get_size()[1]
