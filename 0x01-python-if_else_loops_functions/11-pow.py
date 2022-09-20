#!/usr/bin/python3
def pow(a, b):
	prod = 1
	if b < 0:
		b *= -1
		for i in range (0, b):
			if i < b:
				prod *= a
		prod = 1 / prod
	for i in range(0, b):
		if i < b:
			prod *= a
	return prod

