#!/usr/bin/python3
"""class """
import json


class Base:
    """
    This is the base class that manages the id attribute
    for all other classes in the project.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes an instance of the Base class.

        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of list_dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """string"""
        import json
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)
