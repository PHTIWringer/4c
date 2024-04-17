# Author: Kenneth Hileman
# GitHub username: PHTIWringer
# NOTE: Will not have a ReadMe - Using another IDE
# Date: 04/17/2024
# Description: Program that takes a positive integer parameter as the initial number of a hailstone seqeunce and retunrs how many steps it takes to reach 1.

def hailstone(num):
    '''Takes a positive integer parameter as the initial number of a hailstone sequence and returns how many steps it takes to reach 1'''
    steps = 0
    while num != 1:
        if num % 2 == 0:
            num = num // 2
        else:
            num = (3 * num) + 1
        steps += 1
    return steps
