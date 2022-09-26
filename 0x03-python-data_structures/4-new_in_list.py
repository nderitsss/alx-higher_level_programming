#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    b = list(my_list)
    for i in range(0, len(b)):
        if i == idx:
            b[i] = element
            return b
