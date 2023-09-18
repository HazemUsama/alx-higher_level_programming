#!/usr/bin/python3
"""Rectangle Class Model"""
Base = __import__('base').Base


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


class Rectangle(Base):
    """
    Define the Class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """The width property."""
        return self.__width

    @property
    def height(self):
        """The height property."""
        return self.__height

    @property
    def x(self):
        """The x property."""
        return self.__x

    @property
    def y(self):
        """The y property."""
        return self.__y

    @width.setter
    def width(self, value):
        safeSet(self, 'width', value)

    @height.setter
    def height(self, value):
        safeSet(self, 'height', value)

    @x.setter
    def x(self, value):
        safeSet(self, 'x', value)

    @y.setter
    def y(self, value):
        safeSet(self, 'y', value)
