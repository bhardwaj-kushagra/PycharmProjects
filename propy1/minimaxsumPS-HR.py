#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    minn = arr[0]
    maxN = arr[0]
    summ = arr[0]
    for i in range(4):
        summ += arr[i + 1]
        # print(maxN)
        if arr[i] > arr[i + 1]:
            minn = arr[i + 1]
        elif arr[i] < arr[i + 1]:
            maxN = arr[i + 1]
    # print(f"{summ}{minn}{maxN}")
    print(f"{int(summ - maxN)} {int(summ - minn)}")


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
