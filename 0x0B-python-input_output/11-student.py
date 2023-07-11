#!/usr/bin/python3

"""Definition of a Student"""


class Student:
    """a class Student"""
    def __init__(self, first_name, last_name, age):
        """Initialise the class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student
        instance"""
        if attrs is not None and all(isinstance(item, str) for item in attrs):
            ret = {}
            for p, r in self.__dict__.items():
                if p in attrs:
                    ret[p] = r
            return ret
        else:
            return self.__dict__

    def reload_from_json(self, json):
        ''' Change attributes '''
        for p, r in json.items():
            self.__dict__[p] = r
