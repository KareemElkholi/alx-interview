#!/usr/bin/python3
"""Making Change module"""


def makeChange(coins: list, total: int) -> int:
    """determine the fewest number of coins needed"""
    if total < 1:
        return 0
    coins.sort(reverse=True)
    ans = 0
    for coin in coins:
        while coin <= total:
            total -= coin
            ans += 1
    return -1 if total else ans
