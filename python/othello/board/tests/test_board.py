import unittest

from board import *


class TestBoard(unittest.TestCase):
    def assertFailure(self):
        self.assertEqual(1, 2, "Should fail")

    def checkVictoryW(self):
        board1 = Board("BWWBWWBBW")
        board1.printBoard()

        self.assertEqual(board1.checkVictory(), "W")  # , "Victory not detected"
        # print("Success! Victory for W detected")

    def checkVictoryB(self):
        board1 = Board("BWBWBWBWB")
        board1.printBoard()

        self.assertEqual(board1.checkVictory, "B")  # , "Victory not detected"
        # print("Success! Victory for B detected")

    def checkVictoryNone(self):
        board1 = Board("BWBW-WBWB")
        board1.printBoard()

        self.assertEqual(board1.checkVictory, None)  # , "Victory detected"
        # print("Success! Victory not detected")


if __name__ == "__main__":

    unittest.main()
