#!/usr/bin/python3
"""1-my_list"""


class MyList(list):
    """
    Subclass of list
    """
    def print_sorted(self):
        """prints the list, but sorted"""
        print(sorted(self))
