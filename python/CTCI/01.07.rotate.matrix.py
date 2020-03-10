# Rotate Matrix: Given an image represented by an NxN matrix, where each pixel
# in the image is 4 bytes, write a method to rotate the image by 90 degrees.
# Can you do this in place? Hints: #51, #100

# Caveat: "WHERE EACH PIXEL IS 4 BYTES", what does this mean??!
# Will assume each element a 4-byte int

# APPROACH:
# Since the challenge is to rotate the matrix in place, we can treat the matrix
# as a series of shells or layers. We would rotate the outermost shell and move
# to the next until finishing the innermost

# Within each shell, we would store the value of the matrix at each point, and
# replace it with the value of the matrix at -90 degrees, following a windmill
# spiral of 4 points

# Example: (7x7)
#  .  .  .  .  .  .  .    ==>    .  .  .  .  .  .  .  0
#  .  1  2  3  4  5  .    ==>    . 16  1  2  3  4  .  1
#  . 16  .  .  .  6  .    ==>    . 15  .  .  .  5  .  2
#  . 15  .  .  .  7  .    ==>    . 14  .  .  .  6  .  3
#  . 14  .  .  .  8  .    ==>    . 13  .  .  .  7  .  4
#  . 13 12 11 10  9  .    ==>    . 12 11 10  9  8  .  5
#  .  .  .  .  .  .  .    ==>    .  .  .  .  .  .  .  6
#  0  1  2  3  4  5  6           0  1  2  3  4  5  6

# store 1
# replace 1 with 5
# replace 5 with 9
# replace 9 with 13
# replace 13 with stored 1

# store 2
# replace 2 with 6
# replace 6 with 10
# replace 10 with 14
# replace 14 with stored 2

# continue until row - 1 has been rotated
# move to next inner shell if possible

# An even example: (4x4)
#  .  .  .  .    ==>    .  .  .  .  0
#  .  1  2  .    ==>    . 16  1  .  1
#  . 16  3  .    ==>    .  3  2  .  2
#  .  .  .  .    ==>    .  .  .  .  3
#  0  1  2  3           0  1  2  3

# The number of layers of a n x n matrix = floor(n / 2) + n % 2

# Alternately we can start from the center and move out (easier to calculate perhaps?)


def rotateMatrix(matrix):

    for layer in range(len(matrix) // 2 + len(matrix) % 2):
        topRow = layer
        bottomRow = len(matrix) - layer - 1
        leftCol = layer
        rightCol = len(matrix) - layer - 1

        for x in range(leftCol, rightCol + 1):
            pass


if __name__ == "__main__":

    matrix1 = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
    ]

    rotated1 = [
        [6, 1, 2, 3, 4],
        [11, 7, 8, 9, 5],
        [16, 12, 13, 14, 10],
        [17, 18, 19, 20, 15],
    ]

    assert rotateMatrix(matrix1) == rotated1, "Matrix not rotated correctly"

