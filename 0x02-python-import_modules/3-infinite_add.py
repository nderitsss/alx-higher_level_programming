#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    n = len(argv)
    s1 = 0
    for i in range(1, n):
        s1 = s1 + int(argv[i])
    print(s1)
