#!/usr/bin/python3
import random

# acces to number
number = random.randint(-10, 10)

# check if the number is postive
if number > 0:
    print("{} is positive".format(number))

# check if the number is zero
if number == 0:
    print("{} is zero".format(number))

# check if the number is negative
if number < 0:
    print("{} is negative".format(number))
    