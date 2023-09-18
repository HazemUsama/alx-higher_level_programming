#!/usr/bin/python3
"""Rectangle Class Model"""

from models.base import Base


class Rectangle(Base):
    """
    Define the Class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes attributes
        """
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
        """Sets the value for width"""
        super().safeSet('width', value)

    @height.setter
    def height(self, value):
        """Sets the value for height"""
        super().safeSet('height', value)

    @x.setter
    def x(self, value):
        """Sets the value for x"""
        super().safeSet('x', value)

    @y.setter
    def y(self, value):
        """Sets the value for y"""
        super().safeSet('y', value)
