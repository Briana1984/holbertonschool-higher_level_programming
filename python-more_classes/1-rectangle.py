#!/usr/bin/python3
"""
This module define a empty Rectangle based in the
previous module
"""


class Rectangle:
    """
    This is the empty class
    """

    def __init__(self, width=0, height=0):
        """
        The method constructor:
        parameters:
        width. the purpose is set the value
        height: the purpose is set the value
        """
        self.width = width
        self.heigth = height

    @property
    def width(self):
        """The getter parameters: itself"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter parameters: value"""
        if not isinstance(value, int):
            raise TypeError("width must be an intege")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def heigth(self):
        """The getter parameters: itself"""
        return self.__heigth

    @heigth.setter
    def heigth(self, value):
        """setter parameters: value"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__heigth = value
