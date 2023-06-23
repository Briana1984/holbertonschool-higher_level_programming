#!/usr/bin/python3
"""
create the file
"""


def write_file(filename="", text=""):
    """
    create the file and write
    """
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(text)
        wordlist = text.split(', ')
    numb_char = 0
    for word in wordlist:
        for char in word:
            numb_char += 1
    return numb_char
