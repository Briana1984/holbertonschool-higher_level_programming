#!/usr/bin/python3
"""functions adds 2 integers"""


def add_integer(a, b=98):
    """
    Adds two integers.

    Parameters:
    a (int or float): The first integer.
    b (int or float): The second integer. (default = 98)

    Returns:
    int: The sum of a and b.

    Raises:
    TypeError: If a or b is not an integer or float.

    Examples:
    >>> add_integer(3, 5)
    8

    >>> add_integer(2.5, 4.7)
    7

    >>> add_integer(10)
    108

    >>> add_integer("abc", 5)
    Traceback (most recent call last):
        ...
    TypeError: a must be an integer or b must be an integer
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b


if __name__ == "__main__":
    import doctest
    doctest.testmod()
