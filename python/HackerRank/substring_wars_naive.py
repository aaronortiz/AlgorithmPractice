import re


def findAllSubStringsOfLen(string, length):
    start = 0
    substrings = {}
    for end in range(length, len(string) + 1):
        if not string[start:end] in substrings:
            substrings[string[start:end]] = 1
        else:
            substrings[string[start:end]] += 1
        start += 1

    return substrings


def minion_game(string):
    # your code goes here
    consonantScore = 0
    vowelScore = 0

    for i in range(1, len(string) + 1):
        subStringsOfLenI = findAllSubStringsOfLen(string, i)
        for subString in subStringsOfLenI:
            if re.search("^(a|e|i|o|u|A|E|I|O|U)", subString[0]):
                vowelScore += subStringsOfLenI[subString]
            else:
                consonantScore += subStringsOfLenI[subString]

    if consonantScore == vowelScore:
        print("Draw")
    elif consonantScore > vowelScore:
        print("Stuart", consonantScore)
    else:
        print("Kevin", vowelScore)


if __name__ == "__main__":
    s = input()
    minion_game(s)
