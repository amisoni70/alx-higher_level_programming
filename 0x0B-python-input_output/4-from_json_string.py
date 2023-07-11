#!/usr/bin/python3

"""Function that returns an object represented by JSON"""


import json


def from_json_string(my_str):
    """Returns an obj represented by JSON string"""
    return json.loads(my_str)
