#!/usr/bin/python3

"""Definition of a square that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A class Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialisation"""

        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Retrieves the size of the square"""
        return self.width

    @size.setter
    def size(self, value):
        """Property setter for width & height
        of a square"""
        self.width = value
        self.height = value

    def __str__(self):
        """Prints the square"""

        return ("[Square] ({}) {:d}/{:d} - {:d}".
                format(self.id, self.x, self.y, self.width))
