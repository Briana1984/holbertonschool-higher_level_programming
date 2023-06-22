#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
"""
Square
"""


class Square(Rectangle):
    """
    the subclass
    """

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        return string with area
        """
        return self.__size ** 2

    def __str__(self):
        """
        return string
        """
        return "[Square] " + str(self.__size) + "/" + str(self.__size)