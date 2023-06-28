#!/usr/bin/python3
"""manage id"""


class Base:
    """ content public arg and constructor"""

    __nb_objects = 0

    def __init__(self, id=None):
        """ manage id attribute"""
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
