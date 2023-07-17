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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON representation of a list of
        dictionaries

        Args: list (list of dictionaries)

        Return: JSON String (Str)
        """

        if list_dictionaries is None or list_dictionaries == "[]":
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list represented by json_string

        Returns: Json string representation
        """

        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)
