#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    n = len(sys.argv)
    s1 = 0
    for i in range(0, n):
        s1 = s1 + int((sys.argv[i]))
    print("{}".format((s1)))
