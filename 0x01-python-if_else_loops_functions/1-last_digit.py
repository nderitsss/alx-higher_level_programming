#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    last = number % 10
else:
    last = 10 - (number % 10)
if last == 0:
    print("Last digit of {} is {} and is zero".format(number, last))
elif last > 0 and last < 6:
    print("Last digit of {} is {}".format(number, last), end="")
    print(" and is less than 6 but not 0")
elif last > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, last))
else:
    print("Error")
