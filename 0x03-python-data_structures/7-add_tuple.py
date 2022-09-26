#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    for i in range(0, 2):
        if tuple_a[i] == None:
            tuple_a[i] = 0
        elif tuple_b[i] == None:
            tuple_b[i] = 0
        else :
            tuple_a[i] *= tuple_a[i]
            tuple_b[i] *= tuple_b[i]
    return ((tuple_a[0] + tuple_b[0]),(tuple_a[1] + tuple_b[1]))
