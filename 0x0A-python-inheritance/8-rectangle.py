#!/usr/bin/python3

"""Function that defines BaseGeometry"""


class BaseGeometry:
    """class BaseGeometry"""
    def area(self):
        """Raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates Value"""
        if type(value) != int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")


class Rectangle(BaseGeometry):
    """class Rectangle"""
    def __init__(self, width, height):
        """Instantise"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
