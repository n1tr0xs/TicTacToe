import pygame

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
Colorable = pygame.Color | str | int | tuple[int, int, int, [int]]
