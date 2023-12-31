#!/usr/bin/python3
"""4-print_square"""


def print_square(size):
    """Print a square"""

    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    [print("#" * size) for i in range(size)]
