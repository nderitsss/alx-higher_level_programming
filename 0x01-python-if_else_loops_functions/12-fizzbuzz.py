#!/usr/bin/python3
for i in range(1, 101):
	if i == 100:
		print("Buzz ")
		continue
	if i % 15 == 0:
		print ("FizzBuzz",end = "")
	elif i % 3 == 0:
		print("Fizz",end = "")
	elif i % 5 == 0:
		print("Buzz",end = "")
	else:
		print("{}".format(i), end = "");
	if i != 100:
		print(" ", end = "")
	else:
		continue
	
