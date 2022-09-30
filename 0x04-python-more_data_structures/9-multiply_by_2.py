#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    for key in a_dictionary:
        for values in a_dictionary[key]:
            values *= 2
    return a_dictionary.items()
