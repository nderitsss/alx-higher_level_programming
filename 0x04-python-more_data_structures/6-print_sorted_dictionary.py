#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    b = sorted(a_dictionary.keys())
    for key in b:
        print("{}: {}".format(key, a_dictionary[key]))
