#!/usr/bin/python3
"""One function class_to_json"""


def class_to_json(obj):
    """returns the dictionary description with simple
     data structure (list, dictionary, string, integer and boolean)
    for JSON serialization of an object
    """
    json_dict = {}
    for key, value in obj.__dicit__:
        if isinstance(value, (list, dict, str, int, bool)):
            json_dict[key] = value
    return json_dict
