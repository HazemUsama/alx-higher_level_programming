#!/usr/bin/python3
"""" it's a Square """


class Square:
    """"Still a  Square"""
    def __init__(self, size=0, position=(0, 0)):
        """Initializes a square"""
        self.size = size
        self.position = position

    def area(self):
        """ Retrun the size of the square """
        return self.__size ** 2

    @property
    def size(self):
        """ Size Getter """
        return self.__size

    @size.setter
    def size(self, value):
        """size Setter
        Args:
            value: the new value of size
        """
        if isinstance(value, int):
            if value < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = value
        else:
            raise TypeError('size must be an integer')

    @property
    def position(self):
        """ Position Getter """
        return self.__position

    @position.setter
    def position(self, value):
        """Position Setter
        Args:
            value: the new value of position
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
            not isinstance(value[0], int) or
            not isinstance(value[1], int) or
                value[0] < 0 or value[1] < 0):
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = value

    def my_print(self):
        """ Print squares """
        if self.__size == 0:
            print()
            return
        [print() for i in range(self.__position[1])]
        for i in range(self.__size):
            [print(" ", end="") for j in range(self.__position[0])]
            [print("#", end="") for k in range(self.__size)]
            print()
