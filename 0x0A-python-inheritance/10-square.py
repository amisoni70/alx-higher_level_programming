#!/usr/bin/python3
"""Definition of a square"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """class square"""
    def __init__(self, size):
        """initialisation"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Return the area"""
        return self.__size ** 2
