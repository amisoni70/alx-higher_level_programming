#!/usr/bin/python3

import json


"""Function that returns an object represented by JSON"""


def from_json_string(my_str):
    """Returns an obj represented by JSON string"""
    return json.loads(my_str)
