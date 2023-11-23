#!/usr/bin/python3
"""Module defines the function makeChange"""


def makeChange(coins, total):
    """function determine the fewest
       number of coins needed
       to meet a given amount total
    """

    if total <= 0:
        return 0

    num = 0
    coins.sort(reverse=True)
    for val in coins:
        if total == 0:
            return num
        while val <= total:
            if total % val == 0:
                num = num + (total / val)
                total = 0
            else:
                total = total - val
                num = num + 1
    return -1
