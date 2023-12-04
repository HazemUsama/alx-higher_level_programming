#!/usr/bin/python3
""" function find_peak """


def find_peak(list_of_integers):
    """Define the function"""
    if list_of_integers == []:
        return None
    st = 0
    nd = len(list_of_integers) - 1
    while st < nd:
        if list_of_integers[st] > list_of_integers[st + 1]:
            return list_of_integers[st]
        if list_of_integers[nd] > list_of_integers[nd - 1]:
            return list_of_integers[nd]
        st += 1
        nd -= 1

    return list_of_integers[st]
