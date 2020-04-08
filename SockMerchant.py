#!/bin/python3
"""
Problem Link:
https://www.hackerrank.com/challenges/sock-merchant/problem
"""
import math
import os
import random
import re
import sys
from collections import Counter

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    s = Counter(ar)
    pairs = 0
    for soc in s.values():
        pairs += soc//2
    return pairs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
