#!/usr/bin/python3

"""Function inherits_from"""


def inherits_from(obj, a_class):
    """Return: True - if obj is an instance of a class that
    was inherited from (directly or indirectly) from the
    specified class.
    Otherwise False"""
    return isinstance(obj, a_class) and type(obj) != a_class
