#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    n = len(a)
    ans = 0
    for i in range(n):
        for j in range(n-1):
            if a[j] > a[j+1]:
                tmp = a[j+1]
                a[j+1] = a[j]
                a[j] = tmp
                ans += 1
    print("Array is sorted in " + str(ans) + " swaps.")
    print("First Element:", min(a))
    print("Last Element:", max(a))
    

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
