import math
import os
import random
import re
import sys


#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compareTriplets(a, b):
    # Write your code here
    a_score = 0
    b_score = 0

    for i in range(3):
        if a[i] > b[i]:
            a_score += 1
        elif a[i] < b[i]:
            b_score += 1
        else:
            continue

    return a_score, b_score


if __name__ == '__main__':
    a = [5, 6, 7]
    b = [3, 6, 10]
    compareTriplets(a, b)

#
#
# https://www.hackerrank.com/challenges/compare-the-triplets/problem?isFullScreen=true
