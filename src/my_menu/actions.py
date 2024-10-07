__all__ = [
    'MenuAction',
    'BACK',
    'EXIT',
]


class MenuAction:
    def __init__(self, code: int):
        self._code = code

    def __eq__(self, other: object) -> bool:
        if isinstance(other, MenuAction):
            return self._action == other._action
        return False


BACK = MenuAction(0)  # back to previous menu
EXIT = MenuAction(1)  # exit program
