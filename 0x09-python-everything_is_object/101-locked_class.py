#!/usr/bin/python3
"""Defines a class """


class LockedClass:
    """
    Prevents dynamic creation of attributes

    Attributes:
        first_name (str): first name
    """
    def __init__(self):
        """Creates new instances of Locked Class."""
        self.first_name = "first_name"

    def __setattr__(self, name, value):
        """
        Checks the attribute if it's valid
        """
        if name == 'first_name':
            object.__setattr__(self, name, value)
        else:
            raise AttributeError("'LockedClass' object has no attribute '{}'"
                                 .format(name))
