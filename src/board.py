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

        Returns sign in cell ('X' or 'O' or None)
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
        if value not in ('X', 'O', None):
            raise ValueError('Acceptable values:', ('X', 'O', ''))
        self.cells[x * self.size + y] = value

    def turn(self, x: int, y: int):
        '''
        Controls players turns.

        x - column of board
        y - row of board

        Returns next sign for turn.
        '''
        if self.get(x, y) not in ('O', 'X'):
            self.set(x, y, self._turn)
            self._turn = 'O' if self._turn == 'X' else 'X'

    def is_tie(self):
        '''
        Checks if game is tie.
        '''
        return None not in self.cells

    def is_winner(self, sign: str) -> bool:
        '''
        Returns True if winner have sign.
        '''
        # Three in row
        for i in range(3):
            if self.get(i, 0) == self.get(i, 1) == self.get(i, 2) == sign:
                return True
            if self.get(0, i) == self.get(1, i) == self.get(2, i) == sign:
                return True
        # Diagonals
        if self.get(0, 0) == self.get(1, 1) == self.get(2, 2) == sign:
            return True
        if self.get(2, 0) == self.get(1, 1) == self.get(0, 2) == sign:
            return True
        return False

    def __iter__(self):
        yield from self.cells
