try:
    import pygame
except ImportError:
    print('''
Some required Python modules are not installed:
    - pygame
You can use `pip install -r requirements.txt` to install all required modules.
''')
    exit()

from constants import *
from board import Board
from renderer import Renderer

pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)
clock = pygame.time.Clock()
renderer = Renderer(screen, "white")

def game():
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

game()

pygame.quit()
