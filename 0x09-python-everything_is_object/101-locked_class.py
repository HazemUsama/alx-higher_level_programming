#!/usr/bin/python3
"""Defines a class """


class LockedClass:
    """
    Prevents dynamic creation of attributes

    Attributes:
        first_name (str): first name
    """
    __slots__ = ["first_name"]

    def __init__(self):
        """Creates new instances of Locked Class."""
        self.first_name = "first_name"
