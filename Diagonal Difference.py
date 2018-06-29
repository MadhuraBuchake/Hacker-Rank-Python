#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the diagonalDifference function below.
def diagonalDifference(a):
    a1 = sum(a[i][i] for i in range(n))
    b1 = sum(a[i][n-i-1] for i in range(n))
    return abs(a1-b1)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = []

    for _ in range(n):
        a.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(a)

    fptr.write(str(result) + '\n')

    fptr.close()
