#!/bin/python3

import math
import os
import random
import re
import sys


# countingSort function
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countingSort(arr):
    arrSize = len(arr)
    frequencyArr = [0] * 100
    
    for i in range(arrSize):
        frequencyArr[arr[i]] += 1
    return frequencyArr

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
