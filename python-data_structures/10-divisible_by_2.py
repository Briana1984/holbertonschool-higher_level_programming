#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if not my_list:
        return None
    else:
        div = []
        for i in my_list:
            if i % 2 == 0:
                div.append(True)
            else:
                div.append(False)
        return div
