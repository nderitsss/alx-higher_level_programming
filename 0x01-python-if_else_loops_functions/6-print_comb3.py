#!/usr/bin/python3
for i in range(0,100):
	num1 = i // 10
	num2 = i % 10
	if (num1 == num2 or num1 > num2):
		continue
	elif (i == 89):
		print("89")
		continue
	else:
		print("{}{}".format(num1, num2),end = "")
		print(", ", end = "")
