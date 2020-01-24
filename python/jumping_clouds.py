#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(cloudList):
    jumpCount = 0
    pos = 0
    while pos < len(cloudList) - 1:
        if pos < (len(cloudList) - 2) and cloudList[pos + 2] == 0:
            pos += 2
            jumpCount += 1
        elif pos < (len(cloudList) - 1) and cloudList[pos + 1] == 0:
            pos += 1
            jumpCount += 1
        else:
            return 0

    return jumpCount


if __name__ == "__main__":
    #    fptr = open(os.environ["OUTPUT_PATH"], "w")

    n = 7  # int(input())

    c = [0, 0, 1, 0, 0, 1, 0]  # list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    print(result)

    # fptr.write(str(result) + "\n")

    # fptr.close()
