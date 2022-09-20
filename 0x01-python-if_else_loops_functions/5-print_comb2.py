#!/usr/bin/python3
for i in range(0, 100):
	num1 = i // 10
	num2 = i % 10
	print("{}{}".format(num1, num2), end = "")
	if i == 99:
		continue
	else:
		print(", ",end = "")
