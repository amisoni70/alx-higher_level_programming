#!/usr/bin/python3

"""Function that writes a string to a text file"""


def write_file(filename="", text=""):
    """writes a string to a text file.
    Returns: no of characters written"""
    with open(filename, 'w') as f:
        f.write(text)
        characters = f.tell()
        return characters
