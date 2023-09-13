#!/usr/bin/python3
"""Define a class name Student"""


class Student:
    """Define the class here"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if type(attrs) is list and all(type(item) is str for item in attrs):
            return {item: getattr(self, item)
                    for item in attrs if hasattr(self, item)}
        return self.__dict__

    def reload_from_json(self, json):
        for key, value in json.items():
            setattr(self, key, value)
