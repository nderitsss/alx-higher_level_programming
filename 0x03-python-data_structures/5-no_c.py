#!/usr/bin/python3
def no_c(my_string):
    for i in range(0, len(my_string)):
        if my_string[i] == 'C' or my_string[i] == 'c':
            continue
        else:
            print("{}".format(my_string[i]), end="")
    return ""
