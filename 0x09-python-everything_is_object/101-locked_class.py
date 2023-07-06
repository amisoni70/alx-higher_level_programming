#!/usr/bin/python3
"""Definition of a LockedClass"""


class LockedClass:

    """prevents the  prevents the user from dynamically creating new instance
    attributes except if the new instance attribute is first_name"""

    """Attributes:
    first_name : first name of anything"""

    __slots__ = ["first_name"]

    def __init__(self):

        """Creates an instance of LockedClass"""

        self.first_name = "first_name"
