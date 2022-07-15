#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    # Write your code here
    num = 0
    for i in a:
        num = num ^ i
    return num
  
  # code logic:
  # a = 0
  # [2,3,4,3,2]

  # 000         # a
  # 010         # num
  # 010         # a

  # 010        # a
  # 011         # num
  # 001         # a

  # 001         # a
  # 100         # num
  # 101         # a

  # 101         # a
  # 011         # num
  # 110         # a

  # 110         # a
  # 010         # num
  # 100         # a
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
