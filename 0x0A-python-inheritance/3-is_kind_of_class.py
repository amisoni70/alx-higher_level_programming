#!/usr/bin/python3

"""Function is_kind_of_class"""


def is_kind_of_class(obj, a_class):
    """Return: True- if the obj is an instance of or
    if the obj is an instance of a class thats inherited
    from.
    Otherwise False"""
    return isinstance(obj, a_class)
