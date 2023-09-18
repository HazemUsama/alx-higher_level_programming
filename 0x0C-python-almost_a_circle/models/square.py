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

    @property
    def size(self):
        """The size property."""
        return self._Rectangle__width

    @size.setter
    def size(self, value):
        self._size = value
        if type(value) is not int:
            raise TypeError('width must be an integer')

        if value <= 0:
            raise ValueError('width must be > 0')

        self._Rectangle__width = value
        self._Rectangle__height = value

    def update(self, *args, **kwargs):
        """
        Update attributes
        """
        if len(args) != 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for (key, value) in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """
        Returns the dictionary representation of a Rectangle
        """
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
