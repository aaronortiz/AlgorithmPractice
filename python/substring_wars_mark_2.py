def minion_game(string):
    global consonantScore, vowelScore
    consonantScore = 0
    vowelScore = 0
    vowels = "AEIOU"
    length = len(string)
    for i in range(length):
        if string[i] in vowels:
            vowelScore += length - i
        else:
            consonantScore += length - i

    if consonantScore == vowelScore:
        print("Draw")
    elif consonantScore > vowelScore:
        print("Stuart", consonantScore)
    else:
        print("Kevin", vowelScore)


if __name__ == "__main__":
    s = input()
    minion_game(s)
