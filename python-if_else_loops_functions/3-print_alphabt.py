#!/usr/bin/python3
number_ASCII = range(97, 123)
for i in number_ASCII:
    if i != 101 and i != 113:
        print("{}".format(chr(i)), end="")
     