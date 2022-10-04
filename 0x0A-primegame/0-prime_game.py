#!/usr/bin/python3
"""Prime Game"""


def isWinner(x, nums):
    """ Return: name of the player that won the most rounds.
    If the winner cannot be determined, return None
    """
    res = 0
    for i in range(x):
        res ^= nums[i]
    if (res == 0 or x % 2 == 0):
        return ("Maria")
    else:
        return ("Ben")