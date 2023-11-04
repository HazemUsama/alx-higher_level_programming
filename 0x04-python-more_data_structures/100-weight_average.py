#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:
        return 0
    print(sum(y for x, y in my_list))
    return sum(x * y for x, y in my_list) / sum(y for x, y in my_list)
