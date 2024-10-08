from enum import Enum
import pygame

from constants import *
from board import Board


class Game:
    '''
    Game for 2 local players.
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
        surface: pygame.surface.Surface = None
    ):
        '''
        Initializing the game.

        :param surface: pygame Surface to draw game. Must be given to `run` if None.
        '''
        self._cells = 3
        self._surface = surface
        self._clock = pygame.time.Clock()
        self._board = Board(self._cells)
        self._state = Game.State.Init
        self._score = {'X': 0, 'O': 0, 'Tie': 0}

    def play_again(self) -> None:
        '''
        Resets board and self._state.
        '''
        self._board = Board()
        self._state = Game.State.Running

    def run(
        self,
        surface: pygame.surface.Surface = None,
    ) -> None:
        '''
        Game mainloop.

        :param surface: pygame Surface to draw game.
        :return: 1 if game ended.
        '''
        if surface:
            self._surface = surface
        if self._surface is None:
            raise ValueError("Surface must be pygame Surface.")

        self._state = Game.State.Running
        while True:
            while (event := pygame.event.poll()):
                # close button
                if event.type == pygame.QUIT:
                    exit(0)
                # Escape key
                if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_ESCAPE):
                    return 1
                # is game running ?
                if self._state == Game.State.Running:
                    # left click
                    if (event.type == pygame.MOUSEBUTTONUP) and (event.button == 1):
                        x, y = event.pos
                        cell_dim = self.get_cell_dimension()
                        i, j = x // cell_dim, y // cell_dim
                        self._board.turn(i, j)
                        if (winner := self.check_win_tie()):
                            self._score[winner] += 1
                            self._state = Game.State.Finished
                elif self._state == Game.State.Finished:
                    if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_SPACE):
                        self.play_again()

                self.draw()
            self._clock.tick(10)

    def check_win_tie(self) -> str | None:
        '''
        Checks is game won or tie.

        :return: "X" if "X" won.
        :return: "O" if "O" won.
        :return: "Tie" if game is tie.
        :return: None in other cases.
        '''
        if self._board.is_winner('X'):
            return 'X'
        elif self._board.is_winner('O'):
            return 'O'
        elif self._board.is_tie():
            return 'Tie'
        return None

    '''
    Drawing functions
    '''

    def draw(self) -> None:
        '''
        Renders the game mainloop.

        :param surface: pygame Surface to draw
        '''
        self._surface.fill((0, 0, 0))
        match self._state:
            case Game.State.Running:
                self.draw_board()
            case Game.State.Finished:
                self.draw_gameover()

        pygame.display.flip()

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
        self.draw_grid(grid_color)
        for i in range(self._cells):
            for j in range(self._cells):
                match self._board.get(i, j):
                    case 'X':
                        self.draw_X((i, j), X_color)
                    case 'O':
                        self.draw_O((i, j), O_color)

    def draw_grid(
        self,
        color: Colorable,
    ) -> None:
        '''
        Draws grid.

        :param color: color for grid
        '''
        cell_dim = self.get_cell_dimension()
        # draws vertical lines
        for i in range(1, self._cells):
            pygame.draw.line(
                self._surface, color,
                (cell_dim * i, 0), (cell_dim * i, cell_dim * self._cells)
            )
        # draws horizontal lines
        for i in range(1, self._cells):
            pygame.draw.line(
                self._surface, color,
                (0, cell_dim * i), (cell_dim * self._cells, cell_dim * i)
            )

    def draw_X(
        self,
        cell: tuple[int, int],
        color: Colorable = "red",
    ) -> None:
        '''
        Draws "X".

        :param cell: (column, row) to draw "X"
        :param color: color to draw symbol
        '''
        i, j = cell
        cell_dim = self.get_cell_dimension()
        x = cell_dim * i + cell_dim // 2
        y = cell_dim * j + cell_dim // 2
        length = cell_dim // 2 * .8
        pygame.draw.line(
            self._surface, color,
            (x - length, y - length),
            (x + length, y + length),
        )
        pygame.draw.line(
            self._surface, color,
            (x + length, y - length),
            (x - length, y + length),
        )

    def draw_O(
        self,
        cell: tuple[int, int],
        color: Colorable = "green",
    ) -> None:
        '''
        Draws "O".

        :pararm cell: (column, row) to draw "O"
        :pararm color: color to draw symbol
        '''
        i, j = cell
        cell_dim = self.get_cell_dimension()
        x = cell_dim * i + cell_dim // 2
        y = cell_dim * j + cell_dim // 2
        radius = cell_dim // 2 * .85
        pygame.draw.circle(
            self._surface, color,
            (x, y), radius=radius, width=1
        )

    def draw_gameover(
        self,
    ) -> None:
        '''
        Draws gameover screen.
        '''
        # Scores
        scores = []
        scores.append(self.render_text(
            "Score:",
            "Times New Roman",
            30,
        ))
        for key, val in self._score.items():
            scores.append(self.render_text(
                f"{key:<3}: {val:>7}",
                "Times New Roman",
                20,
            ))
        # calculating coordinates to place rendered Scores
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
            "Times New Roman",
            18,
        ))
        hints.append(self.render_text(
            "Press Esc to go to Menu.",
            "Times New Roman",
            18,
        ))
        # calculating coordinates to place rendered hints
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
        font_name: str = 'Times New Roman',
        font_size: int = 20,
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
        :param font_name: font name
        :param font_size: font size
        :param antialias: antialiasing option
        :param color: color for text
        :param background: background color for text
        :param bold: whether the font should be rendered in bold
        :param italic: whether the font should be rendered in italic
        :param underline: whether the font should be underlined
        :param strikethrough: whether the font should be strikethrough
        :return: pygame.surface.Surface rendered text
        '''
        font = pygame.font.SysFont(font_name, font_size)
        font.set_bold(bold)
        font.set_italic(italic)
        font.set_underline(underline)
        font.set_strikethrough(strikethrough)
        return font.render(text, antialias, color, background)

    '''
    Util methods
    '''

    def get_cell_dimension(
        self,
    ) -> int:
        '''
        Returns cell dimension.

        :return: integer value that corresponds cell width / height
        '''
        return min(self._surface.get_width(), self._surface.get_height()) // self._cells
