from constants import *


class Board:
    def __init__(self, size: int = 3):
        self.size = size
        self.cells = [None] * self.size * self.size
        self._turn = 'X'

    def get(self, x: int, y: int) -> str | None:
        '''
        x - column of board
        y - row of board

        Returns sign in cell ('X' or '0' or None)
        '''
        return self.cells[x * self.size + y]

    def set(self, x: int, y: int, value: str) -> None:
        '''
        This method used for internal operations.
        For player turn use `turn` instead.

        x - column of board
        y - row of board
        value - sign for cell ('X' or '0' or None)
        '''
        if value not in ('X', '0', None):
            raise ValueError('Acceptable values:', ('X', '0', ''))
        self.cells[x * self.size + y] = value

    def turn(self, x: int, y: int):
        '''
        This method controls players turns.

        x - column of board
        y - row of board

        Returns next sign for turn.
        '''
        if self.get(x, y) not in ('0', 'X'):
            self.set(x, y, self._turn)
            self._turn = '0' if self._turn == 'X' else 'X'

        print('Current board:')
        for i in range(self.size):
            for j in range(self.size - 1):

                print(self.cells[j * self.size + i] or ' ', end='|')

            print(self.cells[(self.size - 1) * self.size + i] or ' ')
        print('-' * self.size * self.size)

    def is_draw(self):
        return None not in self.cells

    def get_winner(self) -> str | None:
        for comb in WINNING_COMBINATIONS:
            signs = set(self.get(*pos) for pos in comb)
            if None in signs:
                continue
            if len(signs) == 1:
                return signs.pop()
        return None

    def __iter__(self):
        yield from self.cells
