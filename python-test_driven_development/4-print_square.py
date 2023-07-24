#!/usr/bin/python3
"""This module is composed of a function that prints a square
"""


def print_square(size):
    """This function prints a square formed by the character '#'
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise TypeError("size must be >= 0")
    elif isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for columns in range(size):
        for rows in range(size):
            print("#", end="")
        print()
