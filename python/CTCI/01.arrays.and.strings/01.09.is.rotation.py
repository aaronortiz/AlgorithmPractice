# String Rotation: Assume you have a method isSubst ring which checks if one
# word is a substring of another. Given two strings, 51 and 52, write code to
# check if 52 is a rotation of 51 using only one call to isSubstring (e.g.,
# "waterbottle" is a rotation of"erbottlewat").

# This algorithm is very unintuitive, it depends on the observation that
# appending string 1 to itself and checking whether string 2 is a substring of
# that, is functionally equivalent to checking if string 2 is a rotation of
# string 1s

# My initial approach was to search for the first char in string 2 in string 1
# and test a match of the next characters, taking care to overflow to the
# beginning if needed, until I find either a match or I reach the end of string
# 1. I think this approach is faster too, but more difficult.

# ------------------------------------------------------------------------------
def isSubstring(s1, s2):

    if len(s2) == 0 or len(s2) > len(s1):  # invalid length
        return False
    else:
        for i in range(len(s1)):  # Sliding window method
            if i + len(s2) > len(s1):
                return False
            elif s1[i : i + len(s2)] == s2:
                return True
    return False


# ------------------------------------------------------------------------------
def isRotationOf(s1, s2):
    return isSubstring(s1 + s1, s2)


# ------------------------------------------------------------------------------
if __name__ == "__main__":

    s1 = "Haha"
    s2 = "ah"
    assert isSubstring(s1, s2), "{} is a substring of {}".format(s2, s1)
    print("Success, '{}' is a substring of '{}'".format(s2, s1))

    s1 = "Haha"
    s2 = "ad"
    assert not isSubstring(s1, s2), "{} is not a substring of {}".format(s2, s1)
    print("Success, '{}' is not a substring of '{}'".format(s2, s1))

    s1 = "ad"
    s2 = "Haha"
    assert not isSubstring(s1, s2), "{} is not a substring of {}".format(s2, s1)
    print("Success, '{}' is not a substring of '{}'".format(s2, s1))

    s1 = ""
    s2 = "Haha"
    assert not isSubstring(s1, s2), "{} is not a substring of {}".format(s2, s1)
    print("Success, '{}' is not a substring of '{}'".format(s2, s1))

    s1 = ""
    s2 = ""
    assert not isSubstring(s1, s2), "{} is not a substring of {}".format(s2, s1)
    print("Success, '{}' is not a substring of '{}'".format(s2, s1))

    s1 = "ad"
    s2 = ""
    assert not isSubstring(s1, s2), "{} is not a substring of {}".format(s2, s1)
    print("Success, '{}' is not a substring of '{}'".format(s2, s1))

    s1 = "YouSillyShowoff"
    s2 = "SillyShowoffYou"
    assert isRotationOf(s1, s2), "'{}' is a rotation of '{}'".format(s1, s2)
    print("Success! '{}' is a rotation of '{}'".format(s1, s2))

    s1 = "YouSweetSummerChild"
    s2 = "YouSillyShowoff"
    assert not isRotationOf(s1, s2), "'{}' is not a rotation of '{}'".format(s1, s2)
    print("Success! '{}' is not a rotation of '{}'".format(s1, s2))

