# One Away: There are three types of edits that can be performed on strings:
# insert a character, remove a character, or replace a character. Given two
# strings, write a function to check if they are one edit (or zero edits) away.
# EXAMPLE pale, ple -> true
# pales, pale -> true
# pale, bale -> true
# pale, bake -> false


# APPROACH 1 (WRONG!!!!)
# If I compute the frequency of each character, and then count the differences,
# when there is an insertion, there would be 1 character with a count that is
# 1 greater than the other. A deletion would manifest the same way.
# A replacement would show if there were 2 characters with a count that is 1
# greater than the other. So we can return False if the difference in the count
# of one characters is ever greater than 1, or when there are more than 2 characters
# with a difference greater than 0. Otherwise we would return True

# APPROACH 2
# Base case: compare lengths. If they differ by more than 1 char,
#   then return false
# loop through string1
#   Compare each char with same index of string2.
#   If equal,
#       move to next char
#   Else if next index of string2 = current index of string1, an insertion has occurred
#       add 1 to insertion count
#   Else if next index of string1 = current idnex of string2, a deletion has occurred
#       add 1 to deletion count
#   Else something other than a single insertion or deletion has ocurred
#       return False


def minifiedSolution(string1, string2):

    if abs(len(string1) - len(string2)) > 1:
        return False
    else:

        insertions = 0
        deletions = 0

        for string1Idx in range(len(string1)):
            string2Idx = string1Idx + insertions - deletions

            if string2Idx >= len(string2):  # We've reached the end of string2
                deletions += 1

            elif string1[string1Idx] != string2[string2Idx]:

                if string2Idx + 1 >= len(string2):  # We've reached the end of string2
                    deletions += 1
                elif (
                    string2[string2Idx + 1] == string1[string1Idx]
                ):  # An insertion has occurred
                    insertions += 1
                elif string1Idx + 1 >= len(string1):  # We've reached the end of string1
                    insertions += 1
                elif (
                    string1[string1Idx + 1] == string2[string2Idx]
                ):  # An deletion has occurred
                    deletions += 1
                elif (
                    string1[string1Idx + 1] == string2[string2Idx + 1]
                ):  # a replacement has occurred
                    insertions += 1
                    deletions += 1
                else:  # something else has happened
                    return False

    return deletions + insertions < 3


def isOneEditAway(string1, string2):

    print("Checking '{}' against '{}'.".format(string1, string2))

    if abs(len(string1) - len(string2)) > 1:
        print("The lengths of the strings are more than 1 character different")
        return False
    else:

        insertions = 0
        deletions = 0

        for string1Idx in range(len(string1)):
            string2Idx = string1Idx + insertions - deletions
            try:
                print(
                    "Checking character '{}' against character '{}'".format(
                        string1[string1Idx], string2[string2Idx]
                    )
                )
            except:
                pass
            if string2Idx >= len(string2):  # We've reached the end of string2
                deletions += 1
                print("Characters are different, but string2 has ended")

            elif string1[string1Idx] != string2[string2Idx]:

                if string2Idx + 1 >= len(string2):  # We've reached the end of string2
                    deletions += 1
                    print("Characters are different, but string2 has ended")
                elif (
                    string2[string2Idx + 1] == string1[string1Idx]
                ):  # An insertion has occurred
                    print("Character '{}' was inserted.".format(string2[string2Idx]))
                    insertions += 1
                elif string1Idx + 1 >= len(string1):  # We've reached the end of string1
                    print("Characters are different, but string1 has ended")
                    insertions += 1
                elif (
                    string1[string1Idx + 1] == string2[string2Idx]
                ):  # An deletion has occurred
                    print("Character '{}' was deleted.".format(string1[string1Idx]))
                    deletions += 1
                elif (
                    string1[string1Idx + 1] == string2[string2Idx + 1]
                ):  # a replacement has occurred
                    print(
                        "Character '{}' was replaced by '{}'".format(
                            string1[string1Idx], string2[string2Idx]
                        )
                    )
                    insertions += 1
                    deletions += 1
                else:  # something else has happened
                    print("Strings are too different")
                    return False

    return deletions + insertions < 3


if __name__ == "__main__":

    print("\nTEST CASE 1: equality")

    string1 = "wow"  # input("Enter string 1 of 2: ")
    string2 = "wow"  # input("Enter string 2 of 2: ")

    if isOneEditAway(string1, string2):
        print(
            "'{}' can be converted to '{}' in 1 or less edits.".format(string1, string2)
        )
    else:
        print(
            "'{}' can't be converted to '{}' in 1 or less edits.".format(
                string1, string2
            )
        )

    print("\nTEST CASE 2: insertion at start of string 1")

    string1 = "spam"  # input("Enter string 1 of 2: ")
    string2 = "pam"  # input("Enter string 2 of 2: ")

    if isOneEditAway(string1, string2):
        print(
            "'{}' can be converted to '{}' in 1 or less edits.".format(string1, string2)
        )
    else:
        print(
            "'{}' can't be converted to '{}' in 1 or less edits.".format(
                string1, string2
            )
        )

    print("\nTEST CASE 3: insertion at start of string2")

    string1 = "pam"  # input("Enter string 1 of 2: ")
    string2 = "spam"  # input("Enter string 2 of 2: ")

    if isOneEditAway(string1, string2):
        print(
            "'{}' can be converted to '{}' in 1 or less edits.".format(string1, string2)
        )
    else:
        print(
            "'{}' can't be converted to '{}' in 1 or less edits.".format(
                string1, string2
            )
        )

    print("\nTEST CASE 4: insertion at middle of string 1")

    string1 = "baht"
    string2 = "bat"

    if isOneEditAway(string1, string2):
        print(
            "'{}' can be converted to '{}' in 1 or less edits.".format(string1, string2)
        )
    else:
        print(
            "'{}' can't be converted to '{}' in 1 or less edits.".format(
                string1, string2
            )
        )

    print("\nTEST CASE 5: insertion at middle of string 2")

    string1 = "bat"
    string2 = "baht"

    if isOneEditAway(string1, string2):
        print(
            "'{}' can be converted to '{}' in 1 or less edits.".format(string1, string2)
        )
    else:
        print(
            "'{}' can't be converted to '{}' in 1 or less edits.".format(
                string1, string2
            )
        )

    print("\nTEST CASE 6: insertion at end of string 2")

    string1 = "bat"
    string2 = "bats"

    if isOneEditAway(string1, string2):
        print(
            "'{}' can be converted to '{}' in 1 or less edits.".format(string1, string2)
        )
    else:
        print(
            "'{}' can't be converted to '{}' in 1 or less edits.".format(
                string1, string2
            )
        )

    print("\nTEST CASE 7: insertion at end of string 1")

    string1 = "bats"
    string2 = "bat"

    if isOneEditAway(string1, string2):
        print(
            "'{}' can be converted to '{}' in 1 or less edits.".format(string1, string2)
        )
    else:
        print(
            "'{}' can't be converted to '{}' in 1 or less edits.".format(
                string1, string2
            )
        )

    print("\nTEST CASE 8: string 1 is a substring of 2")

    string1 = "bat"
    string2 = "battery"

    if isOneEditAway(string1, string2):
        print(
            "'{}' can be converted to '{}' in 1 or less edits.".format(string1, string2)
        )
    else:
        print(
            "'{}' can't be converted to '{}' in 1 or less edits.".format(
                string1, string2
            )
        )

    print("\nTEST CASE 9: string 2 is a substring of 1")

    string1 = "battery"
    string2 = "bat"

    if isOneEditAway(string1, string2):
        print(
            "'{}' can be converted to '{}' in 1 or less edits.".format(string1, string2)
        )
    else:
        print(
            "'{}' can't be converted to '{}' in 1 or less edits.".format(
                string1, string2
            )
        )

    print("\nTEST CASE 10: difference in starting char")

    string1 = "pot"
    string2 = "bot"

    if isOneEditAway(string1, string2):
        print(
            "'{}' can be converted to '{}' in 1 or less edits.".format(string1, string2)
        )
    else:
        print(
            "'{}' can't be converted to '{}' in 1 or less edits.".format(
                string1, string2
            )
        )

    print("\nTEST CASE 11: difference in middle char")

    string1 = "pat"
    string2 = "pet"

    if isOneEditAway(string1, string2):
        print(
            "'{}' can be converted to '{}' in 1 or less edits.".format(string1, string2)
        )
    else:
        print(
            "'{}' can't be converted to '{}' in 1 or less edits.".format(
                string1, string2
            )
        )

    print("\nTEST CASE 12: difference in end char")

    string1 = "pal"
    string2 = "pan"

    if isOneEditAway(string1, string2):
        print(
            "'{}' can be converted to '{}' in 1 or less edits.".format(string1, string2)
        )
    else:
        print(
            "'{}' can't be converted to '{}' in 1 or less edits.".format(
                string1, string2
            )
        )

