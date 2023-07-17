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

    def update(self, *args, **kwargs):
        """Updates the Square.

        Args:
        1st Arguement: id attribute
        2nd Arguement: size attribute
        3rd Arguement: x attribute
        4th Arguement: y attribute
        """

        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a = a + 1

        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if key is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """Returns the dictionary representation of a square

        Return: dict, the square"""

        dict = {}
        dict["id"] = self.id
        dict["size"] = self.size
        dict["x"] = self.x
        dict["y"] = self.y
        return dict
