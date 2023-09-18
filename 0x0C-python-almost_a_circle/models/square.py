#!/usr/bin/python3
"Square Class Model"

from models.base import Rectangle


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


