from enum import Enum
import pygame

from board import Board
from constants import *


class Game:
    '''
    Game for 2 players.
    '''
    class State(Enum):
        '''
        Game states.
        Init - initialized.
        Running - players playing the game.
        Winner_X - "X" player won.
        Winner_O - "O" player won.
        Draw - game is draw.
        '''
        Init: int = 0
        Running: int = 1
        Winner_X: int = 2
        Winner_O: int = 3
        Draw: int = 4

    def __init__(self):
        '''
        Initializing the game.

        screen - pygame display to draw the game
        '''
        self.screen = pygame.display.set_mode(WINDOW_SIZE)
        self.clock = pygame.time.Clock()
        self.result_font = pygame.font.SysFont("Times New Roman", 40)
        self.board = Board()
        self.state = Game.State.Init
        self.wins = {'X': 0, 'O': 0, 'Draw': 0}

    def play_again(self):
        self.board = Board()
        self.state = Game.State.Running

    def run(self):
        '''
        Game mainloop.
        '''
        self.state = Game.State.Running
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
        GS = Game.State  # alias
        while (event := pygame.event.poll()):
            # close button
            if event.type == pygame.QUIT:
                return 1
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

            if self.state in (GS.Winner_O, GS.Winner_X, GS.Draw):
                if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_SPACE):
                    self.play_again()
        return 0

    def render(self) -> None:
        '''
        Renders the game mainloop.
        '''
        help_string = "\nPress Space to play again."
        self.screen.fill((0, 0, 0))
        match self.state:
            case Game.State.Running:
                self.draw_board()
            case Game.State.Draw:
                self.draw_text(
                    "Game is draw." + help_string,
                )
            case Game.State.Winner_O:
                self.draw_text(
                    "Winner: O" + help_string,
                )
            case Game.State.Winner_X:
                self.draw_text(
                    "Winner: X" + help_string,
                )

        pygame.display.flip()

    def check_win_draw(self):
        '''
        Returns the state of the game in case of a draw or a win
        Else returns None
        '''
        if self.board.get_winner() == 'X':
            return Game.State.Winner_X
        elif self.board.get_winner() == 'O':
            return Game.State.Winner_O
        elif self.board.is_draw():
            return Game.State.Draw
        return

    '''
    Drawing functions
    '''

    def draw_board(
        self,
        grid_color: Colorable = "white",
        X_color: Colorable = "red",
        O_color: Colorable = "green"
    ) -> None:
        '''
        Draws board
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
                x = CELL_SIZE * i + CELL_SIZE // 2
                y = CELL_SIZE * j + CELL_SIZE // 2
                match self.board.get(i, j):
                    case 'X':
                        self.draw_X(x, y, X_color)
                    case 'O':
                        self.draw_O((x, y), O_color)

    def draw_X(
        self,
        x: int,
        y: int,
        color: Colorable = "red"
    ) -> None:
        '''
        Draws X with center in given coordinates.

        x - x coordinate of the center
        y - y coordinate of the center
        '''
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
        center: tuple[int, int],
        color: Colorable = "green"
    ) -> None:
        '''
        Draws O in given `center`.

        center  - center coordinates for the symbol
        '''
        coef = CELL_SIZE // 2 * .85
        pygame.draw.circle(
            self.screen, color,
            center, coef, 1
        )

    def draw_text(
        self,
        text: str,
        center: tuple[int, int] = None,
        font: pygame.font.Font = None,
        color: Colorable = "white",
        background: Colorable = None,
    ) -> None:
        '''
        Draws multiline text.

        text - [multi]line text to draw
        center - center coordinates of text
        font - font for drawing text
        color - foreground color
        background - background color
        '''
        x, y = center or map(lambda a: a // 2, self.screen.get_size())
        font = font or pygame.font.SysFont("Times New Roman", 20)

        lines = text.split('\n')
        y -= sum(font.size(line)[1] for line in lines) // 2
        for line in lines:
            ren = font.render(
                line, True,
                color, background,
            )
            self.screen.blit(ren, (x - ren.get_size()[0] // 2, y))
            y += ren.get_size()[1]
