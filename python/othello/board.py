class Board:
    # -------------------------------------------------------------------------
    def __init__(self, squares="---------", allowed="WBPO-"):
        self.squares = squares
        self.allowed = allowed

    # -------------------------------------------------------------------------
    def printBoard(self):
        print("╔═══════╗")
        print("║ {} {} {} ║".format(self.squares[0], self.squares[1], self.squares[2]))
        print("║ {} {} {} ║".format(self.squares[3], self.squares[4], self.squares[5]))
        print("║ {} {} {} ║".format(self.squares[6], self.squares[7], self.squares[8]))
        print("╚═══════╝")

    # -------------------------------------------------------------------------
    def hasError(self):
        for square in self.squares:
            if square not in self.allowed:
                print("Character '{}' not allowed".format(square))
                return True

        if len(self.squares) != 9:
            print("Incorrect length for string of square values")
            return True

        return False

    # -------------------------------------------------------------------------
    def checkVictory(self):

        if self.hasError() or "-" in self.squares:
            return None
        else:
            wCount = 0
            bCount = 0
            for square in self.squares:
                if square == "W":
                    wCount += 1
                elif square == "B":
                    bCount += 1

            if wCount > bCount:
                return "W"
            elif bCount > wCount:
                return "B"
            else:
                return None
