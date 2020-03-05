# String Compression: Implement a method to perform basic string compression
# using the counts of repeated characters. For example, the string aabcccccaaa
# would become a2b1c5a3. If the "compressed" string would not become smaller
# than the original string, your method should return the original string. You
# can assume the string has only uppercase and lowercase letters (a -z). Hints:
# #92, # 11 0

# IDEA:
# go through string backwards from the end, counting repetitions and giving
# each a number.


def compressString(s):

    if len(s) < 2:
        return s
    else:

        previousChar = s[len(s) - 2]
        currentRun = 1
        compressedString = ""

        for i in range(len(s) - 2, -1, -1):
            if s[i] != previousChar:
                compressedString = previousChar + str(currentRun) + compressedString
                currentRun = 1
            else:
                currentRun += 1

            previousChar = s[i]

        compressedString = previousChar + str(currentRun) + compressedString

        if len(s) < len(compressedString):
            return s
        else:
            return compressedString


if __name__ == "__main__":

    print("\nTEST CASE: empty string")
    s = ""
    print("'{}' => '{}'".format(s, compressString(s)))

    print("\nTEST CASE: 5 repetitions of a")
    s = "aaaaa"
    print("'{}' => '{}'".format(s, compressString(s)))

    print("\nTEST CASE: increasing repetitions")
    s = "aaaaabbbbbbccccccc"
    print("'{}' => '{}'".format(s, compressString(s)))

    print("\nTEST CASE: single char")
    s = "a"
    print("'{}' => '{}'".format(s, compressString(s)))

    print("\nTEST CASE: no reps")
    s = "abcde"
    print("'{}' => '{}'".format(s, compressString(s)))
