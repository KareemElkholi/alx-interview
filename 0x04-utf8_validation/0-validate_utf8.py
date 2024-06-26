#!/usr/bin/python3
"""UTF-8 Validation module"""


def validUTF8(data):
    """determines if a given data set represents a valid UTF-8 encoding"""
    i = 0
    l = len(data)
    while i < l:
        c = data[i] & 255
        if c >> 7 == 0:
            i += 1
            continue
        r = 0
        if c >> 3 == 30:
            r = 3
        elif c >> 4 == 14:
            r = 2
        elif c >> 5 == 6:
            r = 1
        else:
            return False
        while (r):
            r -= 1
            i += 1
            if i == l or (data[i] & 255) >> 6 != 2:
                return False
        i += 1
    return True
