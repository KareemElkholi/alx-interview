#!/usr/bin/python3
"""UTF-8 Validation module"""


def validUTF8(data):
    """determines if a given data set represents a valid UTF-8 encoding"""
    i = 0
    l = len(data)
    while i < l:
        if data[i] >> 7 == 0:
            i += 1
            continue
        r = 0
        if data[i] >> 3 == 30:
            r = 3
        elif data[i] >> 4 == 14:
            r = 2
        elif data[i] >> 5 == 6:
            r = 1
        else:
            return False
        while (r):
            r -= 1
            i += 1
            if i == l or data[i] >> 6 != 2:
                return False
        i += 1
    return True
