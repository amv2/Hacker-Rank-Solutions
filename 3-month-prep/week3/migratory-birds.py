#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    # Write your code here
    freq = [0] * 6
    # check the frequencies of each type of bird
    for i in arr:
        freq[i] += 1
        
    maximum = 0
    # check the maximum frequency
    for i in range(len(freq)):
        if freq[i] > maximum:
            maximum = freq[i]
            result = i
    
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
