#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the whatFlavors function below.
def whatFlavors(cost, money):

    pairs = {}

    for i in range(len(cost)):
        pairValue = money - cost[i]
        if pairValue in pairs:
            print(pairs[pairValue], i + 1)
            return
        else:
            pairs[cost[i]] = i + 1

    print("No value found")


if __name__ == "__main__":
    # t = int(input())

    # for t_itr in range(t):
    # money = int(input())
    money = 4

    # n = int(input())
    n = 4

    # cost = list(map(int, input().rstrip().split()))
    cost = [2, 2, 4, 3]

    whatFlavors(cost, money)
