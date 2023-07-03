#!/usr/bin/python3
"""Definition of a rectangle"""


class Rectangle:
    """ a class Rectangle that defines a rectangle
    by: (based on 0-rectangle.py)"""

    def __init__(self, width=0, height=0):
        """creates new instances of a rectangle

        Args:
        width(int): creates the width of the rectangle(Defaults to 0)
        height(int): creates the height of the rectangle(Defaults to 0)

        """

        self.width = width
        self.height = height

    @property
    def width(self):

        """a width retriever

        Return: the width(int) of a rectangle

        """

        return self.__width

    @property
    def height(self):

        """a height retriever

        Return: the height(int) of a rectangle

        """

        return self.__height

    @width.setter
    def width(self, value):

        """property setter for width of a rectangle

        Args:
        Value(int) width of a rectangle

        Raises:
        TypeError: if width isn't an integer
        ValueError: if width isn't more or equal to 0

        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):

        """property setter for height of a rectangle

        Args:
        Value(int) height of a rectangle

        Raises:
        TypeError: if height isn't an integer
        ValueError: if height isn't more or equal to 0

        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
