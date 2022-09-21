#!/usr/bin/python3
for i in range(0, 100):
    num1 = i // 10
    num2 = i % 10
    if (i == 99):
        print("99")
        continue
    else:
        print("{}{}, ".format(num1, num2), end="")
