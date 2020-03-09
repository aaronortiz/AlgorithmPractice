#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the twoStrings function below.
def twoStrings(s1, s2):
    # The problem is not well stated, it only needs to check whether the strings have ANY common characters
    if len(s1) == 0 or len(s2) == 0:
        return "NO"
    else:
        for c in range(ord("A"), ord("z") + 1):
            presentInS1 = s1.find(chr(c))
            presentInS2 = s2.find(chr(c))
            if not (presentInS1 == -1 or presentInS2 == -1):
                print(c, chr(c), s1, s2, presentInS1, presentInS2)
                return "YES"

    return "NO"


if __name__ == "__main__":
    # fptr = open(os.environ["OUTPUT_PATH"], "w")

    # q = int(input())

    # for q_itr in range(q):
    #   s1 = input()

    #   s2 = input()

    #   result = twoStrings(s1, s2)

    #   fptr.write(result + "\n")

    # fptr.close()

    print(twoStrings("wouldyoulikefries", "abcabcabcabcabcabc"))
