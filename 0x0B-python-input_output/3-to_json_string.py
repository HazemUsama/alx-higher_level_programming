#!/usr/bin/python3
"""Only one function to_json_string()"""
import json


def to_json_string(my_obj):
    """
    return the JSON representaion of an object
    """
    return json.dumps(my_obj)
