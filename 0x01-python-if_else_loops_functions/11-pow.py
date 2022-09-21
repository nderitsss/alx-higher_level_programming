#!/usr/bin/python3
def pow(a, b):
    prod = 1
    if b < 0:
        b *= -1
        a = 1/a
    for i in range(0, b):
        if i < b:
            prod *= a
    return prod
