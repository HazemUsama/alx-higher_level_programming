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
        """
        Writes the JSON string representation of list_objs to a file
        """
        json_dictionary = []
        for obj in list_objs:
            json_dictionary.append(obj.to_dictionary())

        filename = '{}.json'.format(cls.__name__)
        with open(filename, 'w') as f:
            f.write(cls.to_json_string(json_dictionary))

