#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countTriplets function below.
def countTriplets(arr, ratio):
    count = 0
    foundPairs = {}
    foundTriplets = {}

    for i in arr:
        nextValue = i * ratio

        if i in foundTriplets:
            count += foundTriplets[i]  # An actual new triplet is found

        if i in foundPairs:  # add potential triplet
            if nextValue in foundTriplets:
                foundTriplets[nextValue] += foundPairs[i]
            else:
                foundTriplets[nextValue] = foundPairs[i]

        if nextValue in foundPairs:  # add a potential pair
            foundPairs[nextValue] += 1
        else:
            foundPairs[nextValue] = 1

    return count


if __name__ == "__main__":
    print(countTriplets([1, 1, 1, 1, 1, 1, 1], 1))

    print(
        countTriplets(
            [
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
            ],
            1,
        )
    )

