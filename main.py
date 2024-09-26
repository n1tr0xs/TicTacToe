try:
    import pygame
except ImportError:
    print('''
Some required Python modules are not installed:
    - pygame
You can use `pip install -r requirements.txt` to install all required modules.
''')

from constants import *
from board import Board
from renderer import Renderer


Colorable = pygame.Color | str | int | tuple[int, int, int, [int]]

pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)
clock = pygame.time.Clock()

board = Board()
renderer = Renderer(screen, "white")

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
            x, y = event.pos
            i, j = map(lambda a: a // CELL_SIZE, (x, y))
            board.turn(i, j)

    renderer.draw_board(board)
    pygame.display.flip()

    if (winner := board.is_winner()):
        print(f'{winner} won!')
        running = False
    if board.is_draw():
        print('Draw!')
        running = False

    clock.tick(10)

pygame.quit()
