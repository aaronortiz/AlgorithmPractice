#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    maxSum = -324  # minimum sum if all 36 digits are -9

    for r in range(len(arr) - 2):
        for c in range(len(arr[0]) - 2):
            sum = 0
            sum += arr[r][c]
            sum += arr[r][c + 1]
            sum += arr[r][c + 2]
            sum += arr[r + 1][c + 1]
            sum += arr[r + 2][c]
            sum += arr[r + 2][c + 1]
            sum += arr[r + 2][c + 2]
            print("r", r, "c", c, "sum", sum, "max", maxSum)
            maxSum = max(maxSum, sum)

    return maxSum


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = [
        [-1, -1, 0, -9, 2, 2],
        [-2, -1, -6, -8, -2, -5],
        [-1, -1, -1, -2, -3, -4],
        [-1, -9, -2, -4, -4, -5],
        [-7, -3, -3, -2, -9, -9],
        [-1, -3, -1, -2, -4, -5],
    ]

    # for _ in range(6):
    #    arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
