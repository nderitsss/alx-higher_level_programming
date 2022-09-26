#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    b = []
    for i in my_list:
        if i % 2 == 0:
            b.append(True)
        else:
            b.append(False)
    return b
