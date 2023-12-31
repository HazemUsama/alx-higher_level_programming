#!/usr/bin/python3
"""Base Class Model"""
import json
import os


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
        if list_objs is not None:
            for obj in list_objs:
                json_dictionary.append(obj.to_dictionary())

        filename = '{}.json'.format(cls.__name__)
        with open(filename, 'w', encoding="utf-8") as f:
            f.write(cls.to_json_string(json_dictionary))

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of the JSON string representation
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        filename = f'{cls.__name__}.json'
        instances = []
        dictionary = []
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                dir_str = f.read()
                dictionary = cls.from_json_string(dir_str)
                for dic in dictionary:
                    instances.append(cls.create(**dic))
        return instances
