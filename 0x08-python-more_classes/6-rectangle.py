#!/usr/bin/python3
"""Definition of a rectangle"""


class Rectangle:
    """ a class Rectangle that defines a rectangle
    by: (based on 5-rectangle.py)"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """creates new instances of a rectangle

        Args:
        width(int): creates the width of the rectangle(Defaults to 0)
        height(int): creates the height of the rectangle(Defaults to 0)

        """

        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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

    def area(self):

        """Returns the area of a rectangle"""

        return (self.__width * self.__height)

    def perimeter(self):

        """Returns the perimeter of a rectangle"""

        if self.__width == 0 or self.__height == 0:
            return 0

        return (2 * self.__width) + (2 * self.__height)

    def __str__(self):

        """returns an “informal” and nicely printable string representation
        of a rectangle"""

        rectshape = []

        if self.__width == 0 or self.__height == 0:
            return ""

        for p in range(self.__height):
            for q in range(self.__width):
                rectshape.append('#')
            rectshape.append('\n')

        rectshape.pop()

        return "".join(rectshape)

    def __repr__(self):

        """Returns the string representation of a rectangle"""

        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):

        """Deletes an instance of a class"""

        print("{:s}".format("Bye rectangle..."))
        type(self).number_of_instances -= 1
