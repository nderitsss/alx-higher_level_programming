#!/usr/bin/python3
def multiple_returns(sentence):
    n = len(sentence)
    if n == 0:
        return (0, None)
    p = sentence[0]
    return (n, p)
