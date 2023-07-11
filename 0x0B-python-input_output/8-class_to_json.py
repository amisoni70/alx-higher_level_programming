#!/usr/bin/python3

"""Function for class to JSON"""


def class_to_json(obj):
    """ returns the dictionary description with simple data list"""
    return obj.__dict__
