#!/usr/bin/python3
number_ascii = range(97, 123)
for i in number_ascii:
    if i != 101 and i != 113:
        number_ascii = chr(i)
        print(number_ascii, end="")
     