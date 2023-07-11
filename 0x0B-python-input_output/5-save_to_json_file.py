#!/usr/bin/python3

"""function that writes an Object to a text file
using a JSON Representation"""

import json


def save_to_json_file(my_obj, filename):
    """Returns the JSON representation of the obj"""
    with open(filename, 'w') as f:
        write_data = f.write(json.dumps(my_obj))
