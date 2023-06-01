#!/usr/bin/python3
def uppercase(str):
    for i in str:
        c = ord(i)
        if c <= 122 and c >= 97:
            c = chr(c - 32)
        else:
            c = chr(c)
        print("{}".format(item), end="")
    print("")
