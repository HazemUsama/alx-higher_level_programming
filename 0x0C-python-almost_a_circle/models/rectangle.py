#!/usr/bin/python3
"""Rectangle Class Model"""

from models.base import Base


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
        if isinstance(value, int):
            if value <= 0:
                raise ValueError('width must be > 0')
            else:
                self.__width = value
        else:
            raise TypeError('width must be an integer')

    @height.setter
    def height(self, value):
        if isinstance(value, int):
            if value <= 0:
                raise ValueError('height must be > 0')
            else:
                self.__width = value
        else:
            raise TypeError('height must be an integer')

    @x.setter
    def x(self, value):
        if isinstance(value, int):
            if value < 0:
                raise ValueError('x must be >= 0')
            else:
                self.__width = value
        else:
            raise TypeError('x must be an integer')

    @y.setter
    def y(self, value):
        if isinstance(value, int):
            if value < 0:
                raise ValueError('y must be >= 0')
            else:
                self.__width = value
        else:
            raise TypeError('y must be an integer')

