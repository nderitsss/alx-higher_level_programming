#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    b = list(my_list)
    for i in my_list:
        if i % 2 == 0:
           b[i] = True
        else:
           b[i] = False
    return b
