#!/usr/bin/python3
def raise_exception():
    try:
        raise TypeError("Excepción raised")
    except TypeError as e:
        print(e)
