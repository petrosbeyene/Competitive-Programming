#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    val = arr[-1]
    for i in reversed(range(n-1)):
        if arr[i] < val:
            arr[i+1] = val
            print(*arr)
            break
        else:
            arr[i+1] = arr[i]
            print(*arr)
    if arr[0] > val:
        arr[0] = val
        print(*arr)
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
