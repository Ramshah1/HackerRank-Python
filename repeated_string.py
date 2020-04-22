#!/bin/python3
"""
Problem Link:
https://www.hackerrank.com/challenges/repeated-string/problem
"""

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    size = len(s)
    return ((n//size) * s.count('a')) + s[:n%size].count('a')

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
