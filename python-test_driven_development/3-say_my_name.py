#!/usr/bin/python


def say_my_name(first_name, last_name=""):
    """_summary_

    Args:
        first_name (_type_): _description_
        last_name (str, optional): _description_. Defaults to "".

    Raises:
        TypeError: _description_
        TypeError: _description_
    """
    if not isinstance(first_name, str):
        """_summary_

        Args:
            str (_type_): _description_

        Raises:
            TypeError: _description_
        """
        raise TypeError('first_name must be a string')
    if not isinstance(last_name, str):
        """_summary_

        Args:
            str (_type_): _description_

        Raises:
            TypeError: _description_
        """
        raise TypeError('last_name must be a string')
    if first_name:
        """_summary_
        """
        print("My name is {}".format(first_name))
    else:
        """_summary_
        """
        print("My name is {}".format(last_name))
