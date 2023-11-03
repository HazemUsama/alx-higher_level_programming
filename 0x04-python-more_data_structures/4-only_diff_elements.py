#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    new_set =  {item for item in set_1 if item not in set_2}
    new_set = new_set.union({item for item in set_2 if item not in set_1})
    return new_set
