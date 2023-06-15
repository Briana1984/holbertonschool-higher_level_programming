#!/usr/bin/python3
""" square with the character #"""


def print_square(size):
    """
    Parameters: size of square
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    else:
        if size == 0:
            return
        else:
            for i in range(size):
                print("#" * size)