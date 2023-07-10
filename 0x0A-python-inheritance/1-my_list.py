#!/usr/bin/python3

"""Function that inherits from list"""


class MyList(list):
    """Mylist class"""

    def print_sorted(self):
        """prints the list in ascending order"""
        print(sorted(self))
