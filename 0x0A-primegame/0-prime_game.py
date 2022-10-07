#!/usr/bin/python3
"""Prime Game"""


def isWinner(x, nums):
    """ Return: name of the player that won the most rounds.
    If the winner cannot be determined, return None
    """
    numbers = [0, 0, 1, 1, 2, 2, 3, 3, 4]
    if x < 1 or not nums:
        return None
    res = 0
    for i in nums:
        res ^= numbers[i % x]
    if res > 0:
        return "Maria"
    else:
        return "Ben"
