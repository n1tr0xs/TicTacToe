from enum import Enum
import pygame

from constants import *
import utils
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

    def __init__(self, size: tuple[int, int]):
        '''
        Initializing the game.

        :param screen: pygame display to draw the game
        '''
        self.screen = pygame.display.set_mode(size)
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

    def run(self):
        '''
        Game mainloop.

        :return: 1 if game ended.
        '''
        self.state = Game.State.Running
        while True:
            while (event := pygame.event.poll()):
                # close button
                if event.type == pygame.QUIT:
                    utils.exit(0)
                # Escape key
                if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_ESCAPE):
                    return 1
                # is game running ?
                if self.state == Game.State.Running:
                    # left click
                    if (event.type == pygame.MOUSEBUTTONUP) and (event.button == 1):
                        x, y = event.pos
                        i, j = x // CELL_SIZE, y // CELL_SIZE
                        self.board.turn(i, j)
                        if (winner := self.check_win_tie()):
                            self.score[winner] += 1
                            self.state = Game.State.Finished
                elif self.state == Game.State.Finished:
                    if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_SPACE):
                        self.play_again()

                self.render()
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

    def render(self) -> None:
        '''
        Renders the game mainloop.
        '''
        self.screen.fill((0, 0, 0))
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
        # scores
        surfaces = []
        surfaces.append(self.create_text(
            "Score:",
            font=pygame.font.SysFont("Times New Roman", 30),
        ))
        for key, val in self.score.items():
            surfaces.append(self.create_text(
                f"{key:<3}: {val:>7}",
                font=pygame.font.SysFont("Times New Roman", 20)
            ))
        # calculating x, y to place rendered texts
        screen_width, screen_height = self.screen.get_size()
        center_x, center_y = screen_width // 2, screen_height // 2
        max_width = 0
        total_height = 0
        for surf in surfaces:
            width, height = surf.get_size()
            max_width = max(max_width, width)
            total_height += height

        y = center_y - total_height // 2
        for surf in surfaces:
            width, height = surf.get_size()
            self.screen.blit(surf, (center_x - width // 2, y))
            y += height

        # Hint to play again
        surf = self.create_text(
            "Press Space to play again.",
            font=pygame.font.SysFont("Times New Roman", 18),
        )
        width, height = surf.get_size()
        self.screen.blit(surf, (center_x - width // 2, screen_height - height))

    def create_text(
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
        for i in range(1, self.board.size):
            pygame.draw.line(
                self.screen, grid_color,
                (CELL_SIZE * i, 0), (CELL_SIZE * i, CELL_SIZE * CELLS)
            )
        # draws horizontal lines
        for i in range(1, self.board.size):
            pygame.draw.line(
                self.screen, grid_color,
                (0, CELL_SIZE * i), (CELL_SIZE * CELLS, CELL_SIZE * i)
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
        x = CELL_SIZE * i + CELL_SIZE // 2
        y = CELL_SIZE * j + CELL_SIZE // 2
        coef = CELL_SIZE // 2 * .8
        pygame.draw.line(
            self.screen, color,
            (x - coef, y - coef),
            (x + coef, y + coef)
        )
        pygame.draw.line(
            self.screen, color,
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
        x = CELL_SIZE * i + CELL_SIZE // 2
        y = CELL_SIZE * j + CELL_SIZE // 2
        coef = CELL_SIZE // 2 * .85
        pygame.draw.circle(
            self.screen, color,
            (x, y), coef, 1
        )
