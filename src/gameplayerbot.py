import sys
import pygame
from game import Game
from bot import Bot


class GamePlayerBot(Game):
    '''
    Class for Player vs Bot TicTacToe mode.

    :param player_sign: sign ('X' or 'O') for player
    '''

    def __init__(self, width: int, height: int, fps: int, player_sign: str) -> None:
        super().__init__(width, height, fps)
        self._player_sign = player_sign
        self._bot_sign = 'X' if player_sign == 'O' else 'O'
        self._bot = Bot(self._bot_sign, self._board)

    def play_again(self):
        super().play_again()
        self._bot = Bot(self._bot_sign, self._board)

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
                    return 0
                # is game running ?
                if self._state == Game.State.Running:
                    # left click
                    if (event.type == pygame.MOUSEBUTTONUP)\
                            and (event.button == 1)\
                            and (self._board.get_turn() == self._player_sign):
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

            # bot move
            if (self._state == Game.State.Running) and self._bot.turn():
                if (winner := self.check_win_tie()):
                    self._score[winner] += 1
                    self._state = Game.State.Finished

            self.draw()
            self._clock.tick(self._fps)
