from enum import Enum
import pygame

Colorable = \
    pygame.Color | \
    str | \
    int | \
    tuple[int, int, int] | \
    tuple[int, int, int, int]
