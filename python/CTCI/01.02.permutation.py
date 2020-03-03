# Given two strings, write a method to decide if one is a permutation of the other


def isPermutation(a, b):

    if len(a) != len(b):
        return False
    else:
        if len(a) == 0:  # len(b) would also be 0
            return False
        else:
            sortedA = list(a)
            sortedB = list(b)
            sortedA.sort()
            sortedB.sort()
            if sortedA == sortedB:
                return True

    return False


if __name__ == "__main__":

    print("This program will check if a string is a permutation of another")
    a = input("Enter a string (1 of 2): ")
    b = input("Enter a string (2 of 2): ")

    if isPermutation(a, b):
        print("String", b, "is a permutation of string", a)
    else:
        print("String", b, "is not a permutation of string", a)
