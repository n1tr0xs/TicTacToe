import sys
import pygame
from game import Game


class GameTwoLocalPlayers(Game):
    '''
    Game for 2 local players.

    :pararm width: desired width of the game window.
    :pararm height: desired height of the game window.
    :param cells: desired cells in one row / column.
    '''

    def __init__(self, width: int, height: int, fps: int) -> None:
        super().__init__(width, height, fps)

    def run(self) -> None:
        super().run()

        self._state = Game.State.Running
        while True:
            while (event := pygame.event.poll()):
                # close button
                if event.type == pygame.QUIT:
                    sys.exit(0)
                # Escape key
                if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_ESCAPE):
                    return
                # is game running ?
                if self._state == Game.State.Running:
                    # left click
                    if (event.type == pygame.MOUSEBUTTONUP) and (event.button == 1):
                        x, y = event.pos
                        cell_dim = self.get_cell_dimension()
                        i, j = x // cell_dim, y // cell_dim
                        self._board.turn(i, j)
                        if (winner := self.check_win_tie()):
                            self._score[winner] += 1
                            self._state = Game.State.Finished
                elif self._state == Game.State.Finished:
                    if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_SPACE):
                        self.play_again()

            self.draw()
            self._clock.tick(self._fps)
