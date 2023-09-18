#!/usr/bin/python3
"Square Class Model"

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Define the Class
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Override the str functoin"""
        return f'[Square] ({self.id}) {self.x}/{self.y} - \
{self.width}'

    @@property
    def size(self):
        """The size property."""
        return self.__size

    @size.setter
    def size(self, value):
        self._size = value
        if type(value) is not int:
            raise TypeError('width must be an integer')

        if value <= 0:
            raise ValueError('width must be > 0')

        self.__width = value
        self.__height = value

