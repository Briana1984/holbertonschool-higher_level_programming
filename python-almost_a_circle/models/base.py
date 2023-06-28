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
        """function dictionary"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
