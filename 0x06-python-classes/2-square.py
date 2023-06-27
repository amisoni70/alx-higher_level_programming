#!/usr/bin/python3
"""Definition of a class square"""


class Square:

    """class that defines a square by:(based on 1-square.py)"""

    def __init__(self, size=0):

        """creates new instances of the square

        Args:
        The size of the square"""

        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
