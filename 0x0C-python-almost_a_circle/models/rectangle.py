#!/usr/bin/python3

"""Definition of a Rectangle that inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """a class rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialisation"""
        super().__init__(id)

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """retrives the width

        Returns: the width of the rectangle
        """
        return self.__width

    @property
    def height(self):
        """retrives the height

        Returns: the height of the rectangle
        """
        return self.__height

    @property
    def x(self):
        """retrieves x

        Returns: int x
        """
        return self.__x

    @property
    def y(self):
        """retrives y

        Returns: int y
        """
        return self.__y

    @width.setter
    def width(self, value):
        """property setter for width of a rectangle

        Args: value(int)- width of rectangle
        Raises:
            ValueError: if width is < or = 0
            TypeError: if width is not an int
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """property setter for height of a rectangle

        Args: value(int)- height of rectangle
        Raises:
            ValueError: if height is < or = 0
            TypeError: if height is not an int
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """property setter for x

        Args: value(int)- x
        Raises:
            ValueError: if x is < or = 0
            TypeError: if x is not an int
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """property setter for y

        Args: value(int)- y
        Raises:
            ValueError: if y is < or = 0
            TypeError: if y is not an int
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """defines the area of the rectangle

        Return: Area(int)
        """
        return self.__width * self.__height
