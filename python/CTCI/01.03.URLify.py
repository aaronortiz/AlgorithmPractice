# URLify: Write a method to replace all spaces in a string with '%20: You may
# assume that the string has sufficient space at the end to hold the
# additional characters, and that you are given the "true" length of the
# string. (Note: If implementing in Java, please use a  character array so
# that you can perform this operation in place.


def urlIfy(s):

    newS = ""

    for c in s:
        if c == " ":
            newS += "%20"
        else:
            newS += c

    return newS


if __name__ == "__main__":

    s = input("Enter a string to URLify: ")

    print("URLified string is:", urlIfy(s))
