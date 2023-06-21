#!/usr/bin/python3
"""
sorted a list
"""


class MyList(list):
    """
    this is  subclass of list
    """

    def print_sorted(self):
        """
        in this section sorted the list
        """
        print(sorted(self))


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/1-my_list.txt")
