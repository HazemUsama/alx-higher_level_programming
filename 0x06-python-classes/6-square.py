#!/usr/bin/python3
"""" it's a Square """


class Square:
    """"Still a  Square"""
    def __init__(self, size=0, position=(0, 0)):
        """Initializes a square"""
        if type(size) is int:
            if size < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = size
        else:
            raise TypeError('size must be an integer')
        if type(position[0]) is not int or type(position[1]) is not int or len(position) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
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
        if type(value[0]) is not int or type(value[1]) is not int or len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            __position = value

    def my_print(self):
        if self.__size == 0:
            print()
            return
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()






my_square_1 = Square(3)
my_square_1.my_print()

print("--")

my_square_2 = Square(3, (1, 1))
my_square_2.my_print()

print("--")

my_square_3 = Square(3, (3, 0))
my_square_3.my_print()

print("--")
