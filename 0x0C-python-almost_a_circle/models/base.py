#!/usr/bin/python3
"""Base Class Model"""


class Base:
    """
    Define the Class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    def safeSet(self, name, value):
        """
        Check for type and value before assigning
        """
        if isinstance(value, int):
            if value < 0:
                raise ValueError('{} must be >= 0'.format(name))
            else:
                self.__width = value
        else:
            raise TypeError('{} must be an integer'.format(name))
