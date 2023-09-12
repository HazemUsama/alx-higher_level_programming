#!/usr/bin/python3
"""define a function that adds a new attribute"""


def add_attribute(self, attr_name, value):
    """check if the class can have attributes"""

    if hasattr(self, '__dict__'):
        setattr(self, attr_name, value)
    else:
        raise TypeError("can't add new attribute")
