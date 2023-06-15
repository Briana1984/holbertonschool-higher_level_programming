#!/usr/bin/python3
"""Divides all elements of a matrix."""


def matrix_divided(matrix, div):
    """Function that divides all elements of a matrix"""

    if not all(isinstance(row, list) for row in matrix) or not all(
        isinstance(num, (int, float)) for row in matrix for num in row
    ):
        raise TypeError(
            ("matrix must be a matrix (list of lists) of integers/floats"))

    """ Check if each row of the matrix has the same size """

    if len(set(len(row) for row in matrix)) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    """Validate div input"""
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    """ Validate div value"""
    if div == 0:
        raise ZeroDivisionError("division by zero")
    """ return [[round(elem / div, 2) for elem in item] for item in matrix]"""

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
