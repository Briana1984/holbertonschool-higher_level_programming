#!/usr/bin/python3
"""
reads a text file and prints it to stdout
"""


def read_file(filename=""):
    """statment in mode read"""
    with open(filename, "r", encoding="utf-8") as f:
        read_file = f.read()
    print(read_file, end="")
