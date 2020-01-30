#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isBalanced function below.
def isBalanced(s):
    opening = ["(", "[", "{"]
    closing = [")", "]", "}"]
    matching = {"(": ")", ")": "(", "[": "]", "]": "[", "{": "}", "}": "{"}
    stack = []
    for char in s:
        if char in opening:
            stack.append(char)
        elif char in closing:
            if len(stack) == 0:
                return "NO"
            lastOpening = stack.pop()
            if matching[lastOpening] != char:
                return "NO"

    if len(stack) == 0:
        return "YES"
    else:
        return "NO"


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # t = int(input())

    # for t_itr in range(t):
    # s = input()

    s = "{{}("
    print(isBalanced(s))

    # fptr.write(result + '\n')

    # fptr.close()
