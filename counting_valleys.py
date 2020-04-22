#!/bin/python3
"""
Problem Link:
https://www.hackerrank.com/challenges/counting-valleys/problem
"""
import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    valleys = 0
    sea_level = 0
    for i in s:
        if i == 'U':
            sea_level += 1
        else:
            sea_level -= 1
        if sea_level == 0 and i == 'U':
            valleys += 1
    return valleys


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
