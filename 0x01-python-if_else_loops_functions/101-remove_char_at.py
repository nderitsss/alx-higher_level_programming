#!/usr/bin/python3
def remove_char_at(str, n):
	l = len(str)
	if n < 0:
		return str
	for w in str:
		i = 0
		while (i < l):
			if l == n:
				w = ""
			else:
				return w
			i += 1

