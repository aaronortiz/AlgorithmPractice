# Palindrome Permutation: Given a string, write a function to check if it is a
# permutation of a palin-drome. A palindrome is a word or phrase that is the
# same forwards and backwards. A permutation is a rearrangement of letters. The
# palindrome does not need to be limited to just dictionary words.
# EXAMPLE Input: Tact Coa Output: True (permutations: "taco cat". "atco cta". etc.)


# If a string can be permuted into a palindrome, all of it's characters will appear
# in the string an even number of times, if the string length is even.
# If the string length is odd, one and only of its characters will appear in the
# string an odd number of times.


def isPalindromePermutation(s):

    oddCharacters = {}

    for c in s:
        if c in oddCharacters:
            del oddCharacters[c]
        else:
            oddCharacters[c] = True

    if len(s) % 2 == 0 and len(oddCharacters) == 0:
        return True
    elif len(s) % 2 == 1 and len(oddCharacters) == 1:
        return True
    else:
        return False


if __name__ == "__main__":

    s = input("Enter a string to be tested: ")

    if isPalindromePermutation(s):
        print(s, "can be permuted into a palindrome.")
    else:
        print(s, "can't be permuted into a palindrome.")
