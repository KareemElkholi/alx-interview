#!/usr/bin/python3
"""Prime Game module"""


def isWinner(x, nums):
    """determine who the winner of each game is"""
    ans = 0
    for num in nums:
        count = 0
        arr = [True] * num
        for i in range(1, num):
            if arr[i]:
                n = i
                while n < num:
                    arr[n] = False
                    n += i + 1
                count += 1
        ans += 1 if count % 2 != 0 else -1
    return None if ans == 0 else "Maria" if ans > 0 else "Ben"
