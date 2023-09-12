#!/usr/bin/python3
"""define class MyInt"""


class MyInt(int):
    """invert == and !="""

    def __eq__(self, value):
        return super().__ne__(self, value)

    def __ne__(self, value):
        return super().__eq__(self, value)
