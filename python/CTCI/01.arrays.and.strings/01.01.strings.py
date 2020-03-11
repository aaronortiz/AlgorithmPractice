# Implement an algorithm to determine if a string has all unique characters.
# What if you cannot use additional data structures?

# ------------------------------------------------------------------------------
def areAllCharsUnique(s):

    alreadyEncountered = {}

    for char in s:
        if char in alreadyEncountered:
            return False
        else:
            alreadyEncountered[char] = char

    return True


# ------------------------------------------------------------------------------
def areAllCharsUniqueNoDataStructs(s):

    # This is much less efficient.
    # The idea is to go character by character, searching the remaining string for repetitions
    # The length of the string to be searched will get progressively smaller with each iteration

    for i in range(len(s) - 1):
        if s[i] in s[i + 1 :]:
            return False

    return True


# ------------------------------------------------------------------------------
if __name__ == "__main__":

    s = input("Enter a string: ")

    # I don't want to make assumptions about whether the string is in Unicode...I will assume it is (safest)

    if areAllCharsUnique(s) == True:
        print("The string", s, "is a beautiful snowflake")
    else:
        print("The string", s, "is mainstream and reduntantly repetitive")

    print(
        "Calling the other function with",
        s,
        " gives the result:",
        areAllCharsUniqueNoDataStructs(s),
    )

