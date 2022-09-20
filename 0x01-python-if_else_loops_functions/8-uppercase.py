#!/usr/bin/python3
def uppercase(str):
	for w in str:
		num = ord(w)
		if (num == 32 or num < 97):
			num = num
		else:
			num = num - 32
		print("{}".format(chr(num)),end = "")
	print("{}".format(chr(10)),end = "")
