#!/usr/bin/python3
"""One function class_to_json"""
import json


def class_to_json(obj):
    json_dict = {}
    for key, value in obj.__dicit:
        if isinstance(value, (list, dict, str, int, bool)):
            json_dict[key] = value
    return json_dict
