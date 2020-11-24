#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'countStrings' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def countStrings(s):
    # Write your code here
    result = 0
    length = s.length
    if (s[0]==s[length-1]):
        result++
    for each in s:
        print(each)


    return result


if __name__ == '__main__':
