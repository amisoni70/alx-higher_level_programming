#!/usr/bin/python3

"""Function that reads and prints a text file"""


def read_file(filename=""):
    """reads and prints in stdout"""
    with open(filename) as f:
        read_data = f.read()
        print(read_data, end="")
