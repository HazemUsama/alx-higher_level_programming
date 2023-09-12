#!/usr/bin/python3
"""define a function that adds a new attribute"""


def add_attribute(self, attr, value):
    if hasattr(self, '__dict__'):
        setattr(self, attr, value)
    else:
        raise TypeError("can't add new attribute")
