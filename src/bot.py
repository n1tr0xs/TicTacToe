import sys
from collections import Counter
import pygame
from game import Game
from board import Board


class GamePlayerBot(Game):
    '''
    Class for Player vs Bot TicTacToe mode.

    :param player_sign: sign ('X' or 'O') for player
    '''

    def __init__(self, width: int, height: int, fps: int, player_sign: str) -> None:
        super().__init__(width, height, fps)
        self._player_sign = player_sign
        self._bot_sign = 'X' if player_sign == 'O' else 'O'
        self._bot = Bot(self._bot_sign, self._board)

    def play_again(self):
        super().play_again()
        self._bot = Bot(self._bot_sign, self._board)

    def run(self) -> None:
        super().run()

        self._state = Game.State.Running
        while True:
            while (event := pygame.event.poll()):
                # close button
                if event.type == pygame.QUIT:
                    sys.exit(0)
                # Escape key
                if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_ESCAPE):
                    return
                # is game running ?
                if self._state == Game.State.Running:
                    # left click
                    if (event.type == pygame.MOUSEBUTTONUP)\
                            and (event.button == 1)\
                            and (self._board.get_turn() == self._player_sign):
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

            # bot move
            if (self._state == Game.State.Running) and self._bot.turn():
                if (winner := self.check_win_tie()):
                    self._score[winner] += 1
                    self._state = Game.State.Finished

            self.draw()
            self._clock.tick(self._fps)


class Bot:
    '''
    Bot for TicTacToe game.
    Now supports only 3x3 field.

    :param sign: sign ('X' or 'O') for bot
    :param board: board to play TicTacToe.
    '''

    def __init__(self, sign: str, board: Board) -> None:
        self._sign = sign
        self._player_sign = 'X' if sign == 'O' else 'O'
        self._board = board
        self.generate_checks()

    def generate_checks(self) -> None:
        board_size = self._board.get_size()
        self._checks = []
        # rows
        for i in range(board_size):
            self._checks.append([(i, j) for j in range(board_size)])
        # colums
        for j in range(board_size):
            self._checks.append([(i, j) for i in range(board_size)])
        # diagonals
        self._checks.append(((0, 0), (1, 1), (2, 2)))
        self._checks.append(((0, 2), (1, 1), (2, 0)))

    def check_combination(self, line, sign: str) -> tuple[int, int] | bool:
        '''
        Checks combination to win / prevent player win

        :param line: list of coordinates to make win
        :param sign: which sign to win check
        :return: cell to win on this line if win on next turn is possible. Else False
        '''
        line_signs = [self._board.get(*cell) for cell in line]
        counter = Counter(line_signs)
        if (counter[sign] == 2) and (counter[None] == 1):
            return line[line_signs.index(None)]
        return False

    def turn(self) -> None:
        if self._board.get_turn() != self._sign:
            return
        for check in self._checks:
            if (cell := self.check_combination(check, self._sign)):
                return self._board.turn(*cell)
        for check in self._checks:
            if (cell := self.check_combination(check, self._player_sign)):
                return self._board.turn(*cell)

        optimal_cells = [
            (0, 0),  # left top corner
            (0, 2),  # left bottom corner
            (2, 2),  # right bottom corner
            (2, 0),  # right top corner
            (2, 2),  # center
            (0, 1),  # left center cell
            (1, 0),  # top center cell
            (2, 1),  # right center cell
            (1, 2),  # bottom center cell
        ]
        for cell in optimal_cells:
            if self._board.get(*cell) is None:
                self._board.turn(*cell)
                print(f'Turn to optimal_cell {cell = }')
                return True
        print('No possible moves.')
        return False
