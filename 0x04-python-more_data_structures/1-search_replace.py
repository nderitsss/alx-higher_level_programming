#!/usr/bin/python3
def search_replace(my_list, search, replace):
    b = list(my_list)
    for i in range(0, len(my_list)):
        if b[i] == search:
            b[i] = replace
    return b
