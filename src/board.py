class Board:
    '''
    TicTacToe board object.

    :param size: cells in row / column on the board.
    '''

    def __init__(self, size: int = 3) -> None:
        self._turn = 'X'
        self._size = size
        self._cells = [[None] * self._size for _ in range(self._size)]

    def get(self, i: int, j: int) -> str | None:
        '''
        Returns symbol ('X' or 'O' or None) from cell.

        :param i: row of board
        :param j: column of board

        :return: sign in cell ('X' or 'O' or None)
        '''
        return self._cells[i][j]

    def turn(self, i: int, j: int) -> str:
        '''
        Controls players turns.

        :param i: column of board
        :param j: row of board
        :return: Return next turn sign ('X' or 'O')
        '''
        if self._cells[i][j] is None:
            self._cells[i][j] = self._turn
            self._turn = 'O' if self._turn == 'X' else 'X'
        return self._turn

    def is_tie(self) -> bool:
        '''
        Checks if game is tie.
        You have to check the winner first.

        :return: True if game is tie else False
        '''
        ties = []
        for row in self._cells:
            ties.append(None not in row)
        return all(ties)

    def is_winner(self, sign: str) -> bool:
        '''
        Checks if `sign` won the game.

        :return: True if winner have sign.
        '''
        # Three in row
        for i in range(3):
            if all(self.get(i, j) == sign for j in range(3)):
                return True
            if all(self.get(j, i) == sign for j in range(3)):
                return True
        # Diagonals
        if self.get(0, 0) == self.get(1, 1) == self.get(2, 2) == sign:
            return True
        if self.get(2, 0) == self.get(1, 1) == self.get(0, 2) == sign:
            return True
        return False

    def get_turn(self) -> str:
        '''
        Returns current turn.

        :return: current turn sign ('X' or 'O')
        '''
        return self._turn

    def get_size(self) -> int:
        '''
        Return board size.

        :return: size (one dimension) of the board.
        '''
        return self._size

    def get_row(self, row: int) -> list[str | None]:
        '''
        Returns row of the board.

        :param row: row index to return.
        :return: list of signs ('X' or 'O' or None) in the row.
        '''
        return self._cells[row]

    def get_col(self, col: int) -> list[str | None]:
        '''
        Returns columns of the board.

        :param col: column index to return.
        :return: list of signs ('X' or 'O' or None) in the columns.
        '''
        return [self._cells[i][col] for i in range(self._size)]

    def __str__(self) -> str:
        string = ''
        for i in range(self._size):
            line = ''
            for j in range(self._size):
                line += self._cells[i][j] or '-'
            string += '|'.join(line) + '\n'
        return string

    def __iter__(self) -> str | None:
        for row in self._cells:
            yield from row
