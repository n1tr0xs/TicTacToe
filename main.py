from enum import Enum

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


class Game:
    class GameResult(Enum):
        '''
        Quit - Player want to quit the game.
        Winner_X - X won the game.
        Winner_0 - 0 won the game.
        Draw - The game is over in a draw.
        '''
        Quit: int = 0
        Winner_X: int = 1
        Winner_0: int = 2
        Draw: int = 3

    def __init__(self, screen: pygame.surface.Surface = None, board: Board = None, renderer: Renderer = None):
        self.screen = screen or pygame.display.set_mode(WINDOW_SIZE)
        self.board = board or Board()
        self.renderer = renderer or Renderer()
        self.clock = pygame.time.Clock()

    def run(self):
        while True:
            match self.handle_events():
                case Game.GameResult.Quit:
                    return Game.GameResult.Quit

            self.renderer.draw_board(self.board)
            pygame.display.flip()

            match self.board.get_winner():
                case 'X':
                    return Game.GameResult.Winner_X
                case '0':
                    return Game.GameResult.Winner_0
            if self.board.is_draw():
                return Game.GameResult.Draw

            self.clock.tick(10)

    def handle_events(self) -> str | None:
        result = None
        while (event := pygame.event.poll()):
            # close button
            if event.type == pygame.QUIT:
                return Game.GameResult.Quit
            # Escape
            if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_ESCAPE):
                return Game.GameResult.Quit
            # left click
            if (event.type == pygame.MOUSEBUTTONUP) and (event.button == 1):
                x, y = event.pos
                i, j = x // CELL_SIZE, y // CELL_SIZE
                self.board.turn(i, j)
                result = 'Turn'
        return result


def main():
    screen = pygame.display.set_mode(WINDOW_SIZE)
    renderer = Renderer(screen, "white")

    game = Game(screen=screen, renderer=renderer)

    match game.run():
        case Game.GameResult.Quit:
            return
        case Game.GameResult.Winner_X:
            print('X won!')
        case Game.GameResult.Winner_0:
            print('0 won!')
        case Game.GameResult.Draw:
            print('Draw')
        case _:
            print(r'Unknown game result ¯\_(ツ)_/¯')


if __name__ == '__main__':
    pygame.init()
    main()
    pygame.quit()
