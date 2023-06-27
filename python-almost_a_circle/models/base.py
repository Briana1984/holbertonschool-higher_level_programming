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
