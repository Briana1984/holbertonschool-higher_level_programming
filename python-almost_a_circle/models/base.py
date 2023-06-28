#!/usr/bin/python3
"""manage id"""
import json


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

    """metod static"""
    @staticmethod
    def to_json_string(list_dictionaries):
        """function json_string for list dictionary"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"

        json_string = "["
        for i, dictionary in enumerate(list_dictionaries):
            json_string += "{"
            for key, value in dictionary.items():
                json_string += f'"{key}": {json.dumps(value)}, '
            json_string = json_string.rstrip(", ")
            json_string += "}, "
        json_string = json_string.rstrip(", ")
        json_string += "]"

        return json_string
