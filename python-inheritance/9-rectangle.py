#!/usr/bin/python3
"""
module subclass BaseGeometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    constructor
    """

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        find the area
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Print the rectanle description
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
