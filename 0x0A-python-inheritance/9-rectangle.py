#!/usr/bin/python3

"""Definition of a Rectangle"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """class Rectangle"""
    def __init__(self, width, height):
        """Instantise"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Returns the Area of the Rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Returns a String"""
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
