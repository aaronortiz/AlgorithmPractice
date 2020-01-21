#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    newS = ""
    space = ""
    sList = s.split(" ")
    for word in sList:
        if len(word) > 0:
            newS += space + word[0].upper() + word[1:].lower()
        else:
            newS += space
        space = " "

    return newS


if __name__ == "__main__":
    # fptr = open(os.environ["OUTPUT_PATH"], "w")

    s = input()

    result = solve(s)
    print(result)

    # fptr.write(result + "\n")

    # fptr.close()
