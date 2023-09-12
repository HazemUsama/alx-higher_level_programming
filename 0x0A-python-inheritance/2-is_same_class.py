#!/usr/bin/python3
"""2-is_same_class"""


def is_same_class(obj, a_class):
    """
    Checks if the object is exactly an
     instance of the specified class
    """

    return issubclass(type(obj), a_class)
