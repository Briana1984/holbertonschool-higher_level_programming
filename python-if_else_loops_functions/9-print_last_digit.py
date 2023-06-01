#!/usr/bin/python3
# Prototype
def print_last_digit(number):
    if number < 0:
        i = ((number * -1) % 10)
        print(i, end="")
        return i
    else:
        i = number % 10
        print(i, end="")
        return i