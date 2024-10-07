import pygame
from typing import Union, Tuple, Callable

Color = Union[
    Tuple[int, int, int],
    Tuple[int, int, int, int],
    int,
    pygame.color.Color
]
