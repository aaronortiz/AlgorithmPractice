import math


def repeat(pattern, times):
    result = ""

    for i in range(0, times):
        result += pattern

    return result


numbers = input().split()
rows = int(numbers[0])
cols = rows * 3
middle = math.floor(rows / 2)

# Pattern is centered in a field of "-" of cols length
# On each row before the middle, the pattern is ".|." repeated
# the number of repetitions is (2 * row number) + 1
# since the rest of the string is composed of "-", the number of
# "-" on each side = (cols - (3 * number of above repetitions))/2

for r in range(0, rows):
    patternReps = 0
    minusReps = 0
    if r < middle:
        patternReps = 1 + (2 * r)
        minusReps = math.floor((cols - (3 * patternReps)) / 2)
        print(
            repeat("-", minusReps) + repeat(".|.", patternReps) + repeat("-", minusReps)
        )
    elif r == middle:
        patternReps = 0
        minusReps = math.floor((cols - 7) / 2)
        print(repeat("-", minusReps) + "WELCOME" + repeat("-", minusReps))
    else:
        patternReps = (2 * (rows - r)) - 1
        minusReps = math.floor((cols - (3 * patternReps)) / 2)
        print(
            repeat("-", minusReps) + repeat(".|.", patternReps) + repeat("-", minusReps)
        )
