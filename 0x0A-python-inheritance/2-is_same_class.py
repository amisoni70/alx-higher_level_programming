#!/usr/bin/python3

"""function is_same_class"""


def is_same_class(obj, a_class):
    """Returns true if obj is exactly an instance
    of a specified class"""
    return type(obj) == a_class
