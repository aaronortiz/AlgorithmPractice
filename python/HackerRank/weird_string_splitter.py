def merge_the_tools(string, k):
    # your code goes here
    i = 0
    while i < len(string):
        charCount = {}
        substring = ""
        for j in range(i, i + k):
            if j < len(string):
                if not string[j] in charCount:
                    substring += string[j]
                    charCount[string[j]] = 1
        print(substring)
        i += k


if __name__ == "__main__":
    string, k = input(), int(input())
    merge_the_tools(string, k)
