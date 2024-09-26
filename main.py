try:
    import pygame
except ImportError:
    print('''
Some required Python modules are not installed:
    - pygame
You can use `pip install -r requirements.txt`
''')

from constants import *
from board import Board

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
        running = False
    if (winner := board.is_winner()):
        print(f'{winner} won!')
        running = False

    clock.tick(10)

pygame.quit()
