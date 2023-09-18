#!/usr/bin/python3
"""Base Class Model"""
import json


class Base:
    """
    Define the Class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return '[]'
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        json_dictionary = cls.to_json_string(list_objs)
        filename = '{}.json'.format(cls.__name__)
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(json_dictionary)

