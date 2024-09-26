try:
    import pygame
except ImportError:
    print('''
Some required Python modules are not installed:
    - pygame
You can use `pip install -r requirements.txt`
''')

# constants
CELLS = 3
CELL_SIZE = 80
FIELD_SIZE = CELL_SIZE * CELLS
WINDOW_SIZE = (FIELD_SIZE, FIELD_SIZE)
WINNING_COMBINATIONS = (
    # horizontal
    ((0, 0), (0, 1), (0, 2)),
    ((1, 0), (1, 1), (1, 2)),
    ((2, 0), (2, 1), (2, 2)),
    # vertical
    ((0, 0), (1, 0), (2, 0)),
    ((0, 1), (1, 1), (2, 1)),
    ((0, 2), (1, 2), (2, 2)),
    # diagonal
    ((0, 0), (1, 1), (2, 2)),
    ((0, 2), (1, 1), (2, 0)),
)


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
        print(i, j)
        if self.get(i, j) not in ('0', 'X'):
            self.set(i, j, self._turn)
            self._turn = '0' if self._turn == 'X' else 'X'

    def is_draw(self):
        return None not in self.cells

    def is_winner(self) -> str | None:
        for comb in WINNING_COMBINATIONS:
            signs = set(self.get(*pos) for pos in comb)
            if None in signs:
                continue
            if len(signs) == 1:
                return signs.pop()
        return None

    def __iter__(self):
        yield from self.cells


def draw_X(surface: pygame.surface.Surface, center: tuple[int, int]) -> None:
    '''
    surface - surface to draw symbol
    center  - center coordinates for the symbol
    '''
    x, y = center
    coef = CELL_SIZE // 2 * .8
    pygame.draw.line(
        surface, "white",
        (x - coef, y - coef),
        (x + coef, y + coef)
    )
    pygame.draw.line(
        surface, "white",
        (x + coef, y - coef),
        (x - coef, y + coef)
    )


def draw_0(surface: pygame.surface.Surface, center: tuple[int, int]) -> None:
    '''
    surface - surface to draw symbol
    center  - center coordinates for the symbol
    '''
    coef = CELL_SIZE // 2 * .85
    pygame.draw.circle(
        surface, "white",
        center, coef, 1
    )


def draw_board(surface: pygame.surface.Surface, board: list) -> None:
    # draws vertical lines
    for i in range(1, CELLS):
        pygame.draw.line(
            surface, "white",
            (CELL_SIZE * i, 0), (CELL_SIZE * i, CELL_SIZE * CELLS)
        )
    # draws horizontal lines
    for i in range(1, CELLS):
        pygame.draw.line(
            surface, "white",
            (0, CELL_SIZE * i), (CELL_SIZE * CELLS, CELL_SIZE * i)
        )

    for i in range(board.size):
        for j in range(board.size):
            x = CELL_SIZE * i + CELL_SIZE // 2
            y = CELL_SIZE * j + CELL_SIZE // 2
            match board.get(i, j):
                case 'X':
                    draw_X(surface, (x, y))
                case '0':
                    draw_0(surface, (x, y))


pygame.init()

screen = pygame.display.set_mode(WINDOW_SIZE)
clock = pygame.time.Clock()

board = Board()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
        elif (event.type == pygame.KEYDOWN) and (event.key == pygame.K_ESCAPE):
            running = False
            break
        elif event.type == pygame.MOUSEBUTTONUP:
            # converting coordinates to cells
            i, j = map(lambda a: a // CELL_SIZE, event.pos)
            board.turn(i, j)

    draw_board(screen, board)
    pygame.display.flip()

    if board.is_draw():
        print('Draw!')
    if (winner := board.is_winner()):
        running = False
        print(f'{winner} won!')

    clock.tick(10)

pygame.quit()
