#!/usr/bin/python3
"""Module defines the function makeChange"""


def makeChange(coins, total):
    """function determine the fewest
       number of coins needed
       to meet a given amount total
    """

    if total <= 0:
        return 0

    change = 0
    coins.sort(reverse=True)
    for val in coins:
        if total <= 0:
            break
        num = total // val
        total -= (num * val)
        change += num
    if total != 0:
        return -1
    return change
