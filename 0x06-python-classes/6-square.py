#!/usr/bin/python3
"""" it's a Square """


class Square:
    """"Still a  Square"""
    def __init__(self, size=0, position=(0, 0)):
        """Initializes a square"""
        __size = __size
        __position = position

    def area(self):
        """ Retrun the size of the square """
        return self.__size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            if value < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = value
        else:
            raise TypeError('size must be an integer')

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value[0], int) or
        not isinstance(value[1], int) or len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            __position = value

    def my_print(self):
        if self.__size == 0:
            print()
            return
        [print() for i in range(__position[1])]
        for i in range(self.__size):
            for j in range(self.__size):
                [print(" ", end="") for k in range(__position[0])]
                print("#", end="")
            print()
