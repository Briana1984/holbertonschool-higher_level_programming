#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_sum = 0
    unique_set = set()
    for i in my_list:
        if i not in unique_set:
            unique_set.add(i)
            unique_sum += i
    return unique_sum
