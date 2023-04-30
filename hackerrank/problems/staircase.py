import math
import os
import random
import re
import sys


def staircase(n):
    for stairs in range(1, n + 1):
        print(' ' * (n - stairs) + '#' * stairs)


if __name__ == '__main__':
    # n = int(input().strip())

    staircase(3)
