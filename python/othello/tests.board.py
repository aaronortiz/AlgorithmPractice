from board import *

if __name__ == "__main__":

    board1 = Board("BWWBWWBBW")
    board1.printBoard()

    assert board1.checkVictory() == "W", "Victory not detected"
    print("Success! Victory for W detected")

    board1 = Board("BWBWBWBWB")
    board1.printBoard()

    assert board1.checkVictory() == "B", "Victory not detected"
    print("Success! Victory for B detected")

    board1 = Board("BWBW-WBWB")
    board1.printBoard()

    assert board1.checkVictory() == None, "Victory detected"
    print("Success! Victory not detected")
