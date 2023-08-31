#!/usr/bin/python3
"""" it's a Square """


class Square:
    """"Still a  Square"""
    def __init__(self, size=0):
        """Initializes a square"""
        if type(size) is int:
            if size < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = size
        else:
            raise TypeError('size must be an integer')

    def area(self):
        """ Retrun the size of the square """
        return self.__size ** 2
