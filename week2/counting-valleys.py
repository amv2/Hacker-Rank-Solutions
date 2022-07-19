#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    alt = 0
    valleys = 0
    # check the path
    for i in path:
        # inc / dec the altitude
        if i == "U":
            alt += 1
        else:
            alt += -1
            # if the altitude is below sea level
            # inc the valleys
            if alt == -1:
                valleys += 1
    return valleys

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
