# Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0,
# its entire row and column are set to 0


# ------------------------------------------------------------------------------
def printMatrix(matrix, just=3):
    if not matrix is None:
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                print(str(matrix[row][col]).rjust(just), end="")
            print()


# ------------------------------------------------------------------------------
def attemptSetToZero(matrix, row, col):

    if row >= 0 and row < len(matrix):
        if col >= 0 and col < len(matrix[0]):
            matrix[row][col] = 0
            return True
    return False


# ------------------------------------------------------------------------------
def setRowColumnToZero(matrix, row, col):

    endReached = {"UP": False, "DN": False, "LE": False, "RI": False}

    if not matrix == None and not len(matrix) == 0:
        attemptSetToZero(matrix, row, col)
        for offset in range(1, max(len(matrix), len(matrix[0]))):

            if not endReached["UP"]:
                endReached["UP"] = not attemptSetToZero(matrix, row - offset, col)
            if not endReached["DN"]:
                endReached["DN"] = not attemptSetToZero(matrix, row + offset, col)
            if not endReached["RI"]:
                endReached["RI"] = not attemptSetToZero(matrix, row, col + offset)
            if not endReached["LE"]:
                endReached["LE"] = not attemptSetToZero(matrix, row, col - offset)


# ------------------------------------------------------------------------------
def setRowColumnToZeroDebug(matrix, row, col):

    endReached = {"UP": False, "DN": False, "LE": False, "RI": False}

    if not matrix == None and not len(matrix) == 0:
        attemptSetToZero(matrix, row, col)
        for offset in range(1, max(len(matrix), len(matrix[0]))):
            print("\noffset:", offset)
            if not endReached["UP"]:
                print("Attempting UP")
                endReached["UP"] = not attemptSetToZero(matrix, row - offset, col)
            if not endReached["DN"]:
                print("Attempting DN")
                endReached["DN"] = not attemptSetToZero(matrix, row + offset, col)
            if not endReached["RI"]:
                print("Attempting RI")
                endReached["RI"] = not attemptSetToZero(matrix, row, col + offset)
            if not endReached["LE"]:
                print("Attempting LE")
                endReached["LE"] = not attemptSetToZero(matrix, row, col - offset)


# ------------------------------------------------------------------------------
def zeroMatrix(matrix):

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 0:
                setRowColumnToZero(matrix, row, col)
                return matrix

    return matrix


# ------------------------------------------------------------------------------
if __name__ == "__main__":

    given0 = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25],
    ]

    exp0 = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25],
    ]

    act = zeroMatrix(given0)
    printMatrix(act)
    assert act == exp0, "Smoke test unsuccessful"
    print("Smoke test successful")

    # ------------------------------------------------------------------------------
    given1 = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 0],
    ]

    exp1 = [
        [1, 2, 3, 4, 0],
        [6, 7, 8, 9, 0],
        [11, 12, 13, 14, 0],
        [16, 17, 18, 19, 0],
        [0, 0, 0, 0, 0],
    ]

    act = zeroMatrix(given1)
    printMatrix(act)
    assert act == exp1, "Matrix not zeroed out correctly"
    print("Successful test of bottom right corner")

    # ------------------------------------------------------------------------------
    given2 = [
        [0, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25],
    ]

    exp2 = [
        [0, 0, 0, 0, 0],
        [0, 7, 8, 9, 10],
        [0, 12, 13, 14, 15],
        [0, 17, 18, 19, 20],
        [0, 22, 23, 24, 25],
    ]

    act = zeroMatrix(given2)
    printMatrix(act)
    assert act == exp2, "Matrix not zeroed out correctly"
    print("Successful test of top left corner")

    # ------------------------------------------------------------------------------
    given3 = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 0, 20],
        [21, 22, 23, 24, 25],
    ]

    exp3 = [
        [1, 2, 3, 0, 5],
        [6, 7, 8, 0, 10],
        [11, 12, 13, 0, 15],
        [0, 0, 0, 0, 0],
        [21, 22, 23, 0, 25],
    ]

    act = zeroMatrix(given3)
    printMatrix(act)
    assert act == exp3, "Matrix not zeroed out correctly"
    print("Successful test of 4,4")
