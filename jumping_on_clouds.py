#!/bin/python3
"""
Problem Link:
https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem
"""
import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    max_num = len(c)
    jumps = 0
    idx = 0
    while idx < max_num-1:
        if idx + 2 < max_num and c[idx+2] == 0:
            idx += 2
        else:
            idx += 1
        jumps += 1
    return jumps


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
