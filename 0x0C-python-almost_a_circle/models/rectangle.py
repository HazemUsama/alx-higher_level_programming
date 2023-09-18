#!/usr/bin/python3
"""Rectangle Class Model"""

from models.base import Base


class Rectangle(Base):
    """
    Define the Class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

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
        if type(value) is not int:
            raise TypeError('width must be an integer')

        if value <= 0:
            raise ValueError('width must be > 0')

        self.__width = value

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError('height must be an integer')

        if value <= 0:
            raise ValueError('height must be > 0')

        self.__height = value

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError('x must be an integer')

        if value < 0:
            raise ValueError('x must be >= 0')

        self.__x = value

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError('y must be an integer')

        if value < 0:
            raise ValueError('y must be >= 0')

        self.__y = value

    def area(self):
        """Return the Rectangle area"""
        return self.width * self.height

    def display(self):
        """Display the Rectangle"""
        [print() for i in range(self.y)]
        [print(' ' * self.x + '#' * self.width) for i in range(self.height)]

    def __str__(self):
        """Override the str functoin"""
        return f'[Rectangle] ({self.id}) {self.x}/{self.y} - \
{self.width}/{self.height}'

    def update(self, *args, **kwargs):
        """
        Update attributes
        """
        if args is not None:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.__width = args[1]
            if len(args) >= 3:
                self.__height = args[2]
            if len(args) >= 4:
                self.__x = args[3]
            if len(args) >= 5:
                self.__y = args[4]
        else:
            for key, value in kwargs:
                if hasattr(self, key):
                    setattr(self, key, value)
