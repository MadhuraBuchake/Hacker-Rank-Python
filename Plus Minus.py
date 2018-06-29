#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    p_count = n_count = z_count = 0
    for i in arr:
        if i > 0:
            p_count += 1
        elif i < 0:
            n_count += 1
        else:
            z_count += 1
    print(p_count/n)
    print(n_count/n)
    print(z_count/n)

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
