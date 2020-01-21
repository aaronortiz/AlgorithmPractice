def printCentered(pattern, width):
    result = pattern
    while len(result) < width:
        result = "-" + result + "-"
    print(result)


def print_rangoli(size):
    # your code goes here
    width = 1 + ((size - 1) * 4)
    start = ord("a")
    lines = []

    for offset in range(start + size, start, -1):
        pattern = chr(offset - 1)
        for offset2 in range(offset, start + size):
            pattern = chr(offset2) + "-" + pattern + "-" + chr(offset2)

        printCentered(pattern, width)
        lines.append(pattern)

    lines.pop()
    while len(lines) > 0:
        printCentered(lines.pop(), width)


if __name__ == "__main__":
    n = int(input())
    print_rangoli(n)
