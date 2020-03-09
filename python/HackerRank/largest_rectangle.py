#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the largestRectangle function below.
def largestRectangle(heights):
    global maxConsecutiveRunsByHeight, currConsecutiveRuns, maxArea
    maxConsecutiveRunsByHeight = {}
    currConsecutiveRuns = {}
    maxArea = 0
    previousHeight = 0
    for height in heights:

        if previousHeight > height:
            for cleanup in range(height + 1, previousHeight + 1):
                del currConsecutiveRuns[cleanup]

        for h in range(1, height + 1):
            if h in currConsecutiveRuns:
                currConsecutiveRuns[h] += 1
            else:
                currConsecutiveRuns[h] = 1

            if h in maxConsecutiveRunsByHeight:
                maxConsecutiveRunsByHeight[h] = max(
                    maxConsecutiveRunsByHeight[h], currConsecutiveRuns[h]
                )
            else:
                maxConsecutiveRunsByHeight[h] = currConsecutiveRuns[h]

            maxArea = max(maxArea, maxConsecutiveRunsByHeight[h] * h)

        previousHeight = height

    return maxArea


if __name__ == "__main__":
    # fptr = open(os.environ["OUTPUT_PATH"], "w")

    # n = int(input())

    # h = list(map(int, input().rstrip().split()))

    h = [1, 2, 3, 4, 5]
    print(largestRectangle(h))
    h = [5, 4, 3, 4, 5]
    print(largestRectangle(h))

    # fptr.write(str(result) + "\n")

    # fptr.close()

