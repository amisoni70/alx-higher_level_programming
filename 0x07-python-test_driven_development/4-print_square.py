#!/usr/bin/python3

def print_square(size):

    """ prints a square with the character #

    Args:
    size(int): size of the square (1 side)

    Raises:
    TypeError: if size is not an integer and less than 0
    ValueError: if size isn't more or equal to zero

    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for p in range(size):
        print("#" * size)
