#!/usr/bin/python3
number_ascii = range(97, 123)
for i in number_ascii:
    if i != 101 and i != 113:
        print("{}".format(chr(i)), end="")