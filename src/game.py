from enum import Enum
import pygame

from constants import *
from board import Board


class Game:
    '''
    Game for 2 players.
    '''
    class State(Enum):
        '''
        Game states.
        Init - initialized.
        Running - players playing the game.
        Finished - game finished.
        '''
        Init: int = 0
        Running: int = 1
        Finished: int = 2

    def __init__(
        self,
        surface: pygame.surface.Surface = None,
    ):
        '''
        Initializing the game.

        :param surface: surface to draw the game. Must be given do *run* if None.
        '''
        self._cells = 3
        self._surface = surface
        self.clock = pygame.time.Clock()
        self.board = Board()
        self.state = Game.State.Init
        self.score = {'X': 0, 'O': 0, 'Tie': 0}

    def play_again(self):
        '''
        Resets board and self.state.
        '''
        self.board = Board()
        self.state = Game.State.Running

    def run(self, surface: pygame.surface.Surface):
        '''
        Game mainloop.

        :param surface: surface to draw game.
        :return: 1 if game ended.
        '''
        self._surface = surface
        self.state = Game.State.Running
        while True:
            while (event := pygame.event.poll()):
                # close button
                if event.type == pygame.QUIT:
                    exit(0)
                # Escape key
                if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_ESCAPE):
                    return 1
                # is game running ?
                if self.state == Game.State.Running:
                    # left click
                    if (event.type == pygame.MOUSEBUTTONUP) and (event.button == 1):
                        x, y = event.pos
                        i, j = x // self.get_cell_dimension(), y // self.get_cell_dimension()
                        self.board.turn(i, j)
                        if (winner := self.check_win_tie()):
                            self.score[winner] += 1
                            self.state = Game.State.Finished
                elif self.state == Game.State.Finished:
                    if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_SPACE):
                        self.play_again()

                self.draw()
            self.clock.tick(10)

    def check_win_tie(self):
        '''
        :return: "X" if "X" won.
        :return: "O" if "O" won.
        :return: "Tie" if game is tie.
        :return: None in other cases.
        '''
        if self.board.is_winner('X'):
            return 'X'
        elif self.board.is_winner('O'):
            return 'O'
        elif self.board.is_tie():
            return 'Tie'
        return None

    '''
    Drawing functions
    '''

    def draw(self) -> None:
        '''
        Renders the game mainloop.
        '''
        self._surface.fill((0, 0, 0))
        match self.state:
            case Game.State.Running:
                self.draw_board()
            case Game.State.Finished:
                self.draw_gameover()

        pygame.display.flip()

    def draw_gameover(self):
        '''
        Draws gameover screen.
        '''
        # Scores
        scores = []
        scores.append(self.render_text(
            "Score:",
            font=pygame.font.SysFont("Times New Roman", 30),
        ))
        for key, val in self.score.items():
            scores.append(self.render_text(
                f"{key:<3}: {val:>7}",
                font=pygame.font.SysFont("Times New Roman", 20)
            ))
        # calculating x, y to place rendered texts
        screen_width, screen_height = self._surface.get_size()
        center_x, center_y = screen_width // 2, screen_height // 2
        total_height = sum(surf.get_height() for surf in scores)
        y = center_y - total_height // 2
        for surf in scores:
            width, height = surf.get_size()
            self._surface.blit(surf, (center_x - width // 2, y))
            y += height

        # Hints
        hints = []
        hints.append(self.render_text(
            "Press Space to play again.",
            font=pygame.font.SysFont("Times New Roman", 18),
        ))
        hints.append(self.render_text(
            "Press Esc to go to Menu.",
            font=pygame.font.SysFont("Times New Roman", 18),
        ))
        # calculating x, y to place rendered texts
        screen_width, screen_height = self._surface.get_size()
        center_x, center_y = screen_width // 2, screen_height // 2
        total_height = sum(surf.get_height() for surf in hints)
        y = self._surface.get_height()
        for surf in hints[::-1]:
            width, height = surf.get_size()
            y -= height
            self._surface.blit(surf, (center_x - width // 2, y))

    def render_text(
        self,
        text: str,
        font: pygame.font.Font = None,
        antialias: bool = True,
        color: Colorable = "white",
        background: Colorable = None,
        bold: bool = False,
        italic: bool = False,
        underline: bool = False,
        strikethrough: bool = False,
    ) -> pygame.surface.Surface:
        '''
        Creates text surface.

        :param text: text to draw
        :param font: font for text
        :param antialias: antialiasing option
        :param color: color for text
        :param background: background color for text
        :param bold: whether the font should be rendered in bold
        :param italic: whether the font should be rendered in italic
        :param underline: whether the font should be underlined
        :param strikethrough: whether the font should be strikethrough
        :return: pygame.surface.Surface rendered text
        '''
        font = font or pygame.font.SysFont("Times New Roman", 20)
        font.set_bold(bold)
        font.set_italic(italic)
        font.set_underline(underline)
        font.set_strikethrough(strikethrough)
        return font.render(text, antialias, color, background)

    def get_cell_dimension(self):
        if self._surface is None:
            return 0
        return min(self._surface.get_width(), self._surface.get_height()) // self._cells

    def draw_board(
        self,
        grid_color: Colorable = "white",
        X_color: Colorable = "red",
        O_color: Colorable = "green"
    ) -> None:
        '''
        Draws board

        :param grid_color: color for grid
        :param X_color: color for sign "X"
        :param O_color: color for sign "O"
        '''
        # draws vertical lines
        cell_width = self.get_cell_dimension()
        cell_height = self.get_cell_dimension()
        for i in range(1, self.board.size):
            pygame.draw.line(
                self._surface, grid_color,
                (cell_width * i, 0), (cell_width * i, cell_height * self._cells)
            )
        # draws horizontal lines
        for i in range(1, self.board.size):
            pygame.draw.line(
                self._surface, grid_color,
                (0, cell_height * i), (cell_width * self._cells, cell_height * i)
            )
        # draws signs on the board
        for i in range(self.board.size):
            for j in range(self.board.size):
                match self.board.get(i, j):
                    case 'X':
                        self.draw_X((i, j), X_color)
                    case 'O':
                        self.draw_O((i, j), O_color)

    def draw_X(
        self,
        cell: tuple[int, int],
        color: Colorable = "red"
    ) -> None:
        '''
        Draws "X".

        :param cell: (column, row) to draw "X"
        :param color: color to draw symbol
        '''
        i, j = cell
        x = self.get_cell_dimension() * i + self.get_cell_dimension() // 2
        y = self.get_cell_dimension() * j + self.get_cell_dimension() // 2
        coef = self.get_cell_dimension() // 2 * .8
        pygame.draw.line(
            self._surface, color,
            (x - coef, y - coef),
            (x + coef, y + coef)
        )
        pygame.draw.line(
            self._surface, color,
            (x + coef, y - coef),
            (x - coef, y + coef)
        )

    def draw_O(
        self,
        cell: tuple[int, int],
        color: Colorable = "green"
    ) -> None:
        '''
        Draws "O".

        :pararm cell: (column, row) to draw "O"
        :pararm color: color to draw symbol
        '''
        i, j = cell
        x = self.get_cell_dimension() * i + self.get_cell_dimension() // 2
        y = self.get_cell_dimension() * j + self.get_cell_dimension() // 2
        coef = self.get_cell_dimension() // 2 * .85
        pygame.draw.circle(
            self._surface, color,
            (x, y), coef, 1
        )
