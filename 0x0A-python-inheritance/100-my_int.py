#!/usr/bin/python3
"""define class MyInt"""


class MyInt(int):
    """invert == and !="""

    def __eq__(self, value):
        return super().__ne__(value)

    def __ne__(self, value):
        return super().__eq__(value)


my_i = MyInt(3)
print(my_i)
print(my_i == 3)
print(my_i != 3)
