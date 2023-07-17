#!/usr/bin/python3

"""Definition of a class named Base. This class will be the “base” of all other
classes in this project."""
import json


class Base:
    """Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialisation

        Args:
        id (int): object id. Defaults to none.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
