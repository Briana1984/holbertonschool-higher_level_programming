#!/usr/bin/python3
""" appends a string at the end"""


def append_write(filename="", text=""):
    """
    Parameters: filename is the file, text is the string
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
