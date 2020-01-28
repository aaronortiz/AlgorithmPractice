#!/bin/python3

import math
import os
import random
import re
import sys


def getSubstringsOfLengthN(string, length):
    substrings = []

    for i in range(length, len(string)):
        if not string[i - length : i] in substrings:
            substrings.append(string[i - length : i])

    return substrings


def getLongerAndShorter(string1, string2):
    longString = ""
    shortString = ""
    if len(s1) < len(s2):
        longString = s2
        shortString = s1
    else:
        longString = s1
        shortString = s2

    return longString, shortString


# Complete the twoStrings function below.
def twoStrings(s1, s2):
    # 1st check if they share any letters
    # 2nd do a 2 char window pass of shorter of 2 strings across long one
    # nth keep increasing window until entire string is used
    # use short circuit to stop most worst case scenarios
    if len(s1) == 0 or len(s2) == 0:
        return "NO"
    else:
        longString, shortString = getLongerAndShorter(s1, s2)
        for windowSize in range(1, len(shortString) + 1):
            stringsOfWindowSize = getSubstringsOfLengthN(longString, windowSize)
            for j in range(windowSize, len(shortString)):
                if shortString[j - windowSize : j] in stringsOfWindowSize:
                    return "YES"
    return "NO"


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + "\n")

    fptr.close()
