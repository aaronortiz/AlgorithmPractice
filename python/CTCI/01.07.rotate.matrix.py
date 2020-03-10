# Rotate Matrix: Given an image represented by an NxN matrix, where each pixel
# in the image is 4 bytes, write a method to rotate the image by 90 degrees.
# Can you do this in place? Hints: #51, #100

# Caveat: "WHERE EACH PIXEL IS 4 BYTES", what does this mean??!
# Will assume each element a 4-byte int

# APPROACH:
# Since the challenge is to rotate the matrix in place, we can treat the matrix
# as a series of shells or layers. We would rotate the outermost shell and move
# to the next until finishing the innermost

# Since the matrix is square, we can treat each shell as a series of 4 lines
# with each points corresponding with 3 others if we rotate the matrix 90 degrees.

# These 4 point correspond:
#  a  .  .  d
#  .        .
#  .        .
#  b  .  .  c

# As do these:
#  .  a  .  .
#  .        d
#  b        .
#  .  .  c  .

# And these:
#  .  .  a  .
#  b        .
#  .        d
#  .  c  .  .

# We store the value of the a, the first of these, and replace it with b, the value that is
# at -90 degrees, and follow suit with c and d, following a windmill spiral of 4 points

# Then we would move to the 4 points adjacent to the ones we just replaced, until
# the entire shell is rotated (see example)

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

# ------------------------------------------------------------------------------
def printMatrix(matrix):
    if not matrix is None:
        for l in range(len(matrix)):
            print(matrix[l])


# ------------------------------------------------------------------------------
def rotateMatrix(matrix):

    # Check for invalid matrix
    if matrix == None or len(matrix) == 0 or not len(matrix) == len(matrix[0]):
        return matrix

    # Rotate one "onion layer" at a time, moving from out to in
    for layer in range(len(matrix) // 2 + len(matrix) % 2):

        start = layer  # Find start index (left column & top row)
        end = len(matrix) - layer - 1  # Find end index (right column & bottom row)

        for x in range(start, end):
            # use a windmill pattern and a temp var to rotate in place
            offset = x - start
            temp = matrix[start][x]  # indices are assumed to be [row][col]
            # maps value to top row from left col
            matrix[start][x] = matrix[end - offset][start]
            # maps value to left col from bottom row
            matrix[end - offset][start] = matrix[end][end - offset]
            # maps value to bottom row from right col
            matrix[end][end - offset] = matrix[start + offset][end]
            # maps value to right column from top row
            matrix[start + offset][end] = temp

    return matrix


# ------------------------------------------------------------------------------
def rotateMatrixDebug(matrix):

    if len(matrix) == 0:
        print("Matrix empty")
        return matrix
    elif not len(matrix) == len(matrix[0]):
        print("Not a square matrix")
        return matrix

    for layer in range(len(matrix) // 2 + len(matrix) % 2):
        topRow = layer
        bottomRow = len(matrix) - layer - 1
        leftCol = layer
        rightCol = len(matrix) - layer - 1

        print(
            "\n\n>>>>>>>>>>>>>>>>TR:",
            topRow,
            "BR:",
            bottomRow,
            "LC:",
            leftCol,
            "RC:",
            rightCol,
        )

        for x in range(leftCol, rightCol):

            offset = x - leftCol

            print("\nx:", x, "Before:")
            printMatrix(matrix)

            print("Setting temp = {},{}({})".format(topRow, x, matrix[topRow][x]))
            temp = matrix[topRow][x]

            print(
                "replacing {},{}({}) with {},{}({})".format(
                    topRow,
                    x,
                    matrix[topRow][x],
                    bottomRow - offset,
                    leftCol,
                    matrix[bottomRow - offset][leftCol],
                )
            )
            matrix[topRow][x] = matrix[bottomRow - offset][leftCol]

            print(
                "replacing {},{}({}) with {},{}({})".format(
                    bottomRow - offset,
                    leftCol,
                    matrix[bottomRow - offset][leftCol],
                    bottomRow,
                    rightCol - offset,
                    matrix[bottomRow][rightCol - offset],
                )
            )
            matrix[bottomRow - offset][leftCol] = matrix[bottomRow][rightCol - offset]

            print(
                "replacing {},{}({}) with {},{}({})".format(
                    bottomRow,
                    rightCol - offset,
                    matrix[bottomRow][rightCol - offset],
                    topRow + offset,
                    rightCol,
                    matrix[topRow + offset][rightCol],
                )
            )
            matrix[bottomRow][rightCol - offset] = matrix[topRow + offset][rightCol]

            print(
                "replacing {},{}({}) with {},{}({})".format(
                    topRow + offset,
                    rightCol,
                    matrix[topRow + x][rightCol],
                    topRow,
                    x,
                    temp,
                )
            )
            matrix[topRow + offset][rightCol] = temp
            print("after:")
            printMatrix(matrix)
    return matrix


if __name__ == "__main__":

    matrix1 = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25],
    ]

    rotated1 = [
        [21, 16, 11, 6, 1],
        [22, 17, 12, 7, 2],
        [23, 18, 13, 8, 3],
        [24, 19, 14, 9, 4],
        [25, 20, 15, 10, 5],
    ]

    assert rotateMatrix(matrix1) == rotated1, "Matrix not rotated correctly"
    print("5x5 matrix rotated successfully")
    printMatrix(matrix1)

    assert rotateMatrix([]) == [], "Matrix is empty"
    assert rotateMatrix(None) == None, "Matrix is None"
    print("Empty matrix averted")

    matrix2 = [[1]]
    rotated2 = [[1]]
    assert rotateMatrix(matrix2) == rotated2, "Matrix not rotated correctly"
    print("1x1 matrix 'rotated' successfully")
    printMatrix(matrix2)

    matrix3 = [[1, 2], [3, 4]]
    rotated3 = [[3, 1], [4, 2]]
    assert rotateMatrix(matrix3) == rotated3, "Matrix not rotated correctly"
    print("2x2 matrix rotated successfully")
    printMatrix(matrix3)

    matrix4 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    rotated4 = [[13, 9, 5, 1], [14, 10, 6, 2], [15, 11, 7, 3], [16, 12, 8, 4]]
    assert rotateMatrix(matrix4) == rotated4, "Matrix not rotated correctly"
    print("4x4 matrix rotated successfully")
    printMatrix(matrix4)
