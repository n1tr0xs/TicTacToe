class Board:
    '''
    TicTacToe board object.
    '''

    def __init__(self, size):
        '''
        Initializing board.

        :param size: cells in row / column on the board.
        '''
        self._size = size
        self._cells = [None] * self._size * self._size
        self._turn = 'X'

    def get(self, x: int, y: int) -> str | None:
        '''

        :param x: column of board
        :param y: row of board

        :return: sign in cell ('X' or 'O' or None)
        '''
        return self._cells[x * self._size + y]

    def set(self, x: int, y: int, value: str) -> None:
        '''
        This method used for internal operations.
        For player turn use `turn` instead.

        :param x: column of board
        :param y: row of board
        :param value: sign for cell ('X' or '0' or None)
        '''
        if value not in ('X', 'O', None):
            raise ValueError('Acceptable values:', ('X', 'O', ''))
        self._cells[x * self._size + y] = value

    def turn(self, x: int, y: int) -> None:
        '''
        Controls players turns.

        :param x: column of board
        :param y: row of board
        '''
        if self.get(x, y) not in ('O', 'X'):
            self.set(x, y, self._turn)
            self._turn = 'O' if self._turn == 'X' else 'X'

    def is_tie(self) -> bool:
        '''
        Checks if game is tie.
        You have to check the winner first.

        :return: True if game is tie else False
        '''
        return None not in self._cells

    def is_winner(self, sign: str) -> bool:
        '''
        Checks if `sign` won the game.

        :return: True if winner have sign.
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
        yield from self._cells
