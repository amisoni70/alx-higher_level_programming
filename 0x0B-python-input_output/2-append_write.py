#!/usr/bin/python3

"""Function that appends a string at the end of a text file"""


def append_write(filename="", text=""):
    """appends a string at the end of .txt file
    Return: no of characters added"""
    with open(filename, 'a') as f:
        characters = f.write(text)
    return characters
