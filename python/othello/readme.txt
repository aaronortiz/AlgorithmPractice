OTHELLO

So...I want to implement a decision tree pruning algorithm in Python for a 
text-based Othello.

I am starting with a 3x3 version of it. This can be scaled up, maybe?

REPRESENTATION:
    Boards are represented with strings:

    "-" represents an empty square
    "B" is a square with the Othello piece's black side on top
    "W" is a square with the Othello piece's white side on top

    the 3x3 board:
    ╔═══════╗
    ║ - B - ║
    ║ - W B ║
    ║ - W W ║
    ╚═══════╝

is represented as "-BW-W--WW"

STORING STRATEGY:
    When storing game strategy though, the color of the piece does not matter. 
    What does matter is whether the piece belongs to the current player or to 
    the opponent

    so...
    "P" is a square with an Othello piece belonging to the current player
    "O" is a square belonging to the oponent 

    If the current player is White, then the same board above would be stored 
    as:
        ╔═══════╗
        ║ - O - ║
        ║ - P O ║
        ║ - P P ║
        ╚═══════╝

MOVES:
    Moves are represented by coordinates, the move to place a piece in the top 
    right of the board, would be represented as 0,2

    This is a desirable move because it captures the middle right piece

    This would be added to a strategy data structure as:
    ["-O--PO-PP"][0][2] = "C"

    If instead the player were to place a piece on the bottom left square, then 
    the opponent can capture the middle square. Should that happen, we would 
    add this to the strategy data structure this way:
    ["-O--PO-PP"][0][2] = "C"

STORING ROTATIONS:
    If we rotate each board by 90° or flip it by the horizontal or vertical 
    axis or both we will find that the strategy for the best move is the same.
    So each board is part of a set of 4 * 2 * 2 = 16 functionally equivalent
    boards.

    There are only 3 strategies once we eliminate the ones that can be mirrored 
    or rotated into one another:
        1. Place a piece in the center square (A TERRIBLE MOVE BTW)
        2. Place a piece in the middle of an edge (CAN BE OK)
        3. Place a piece in one of the corners (USUALLY THE BEST MOVE)

    We could store all 4 rotations and 2 mirrors every time there is an 
    opportunity to learn...but that would grow the strategy datastructure by
    powers of 16. 
    
    In order to reduce the burden of memory space and processing time we will
    compute all 16 equivalent boards when we wish to store or retrieve a board
    but then we will score them in such a way as to produce a unique score for
    each of the 16.
 
    We will score a board in this way:

    If a square in the board has a piece, assign 0 points

    If a square in the board is empty, score it with this many points according
    to where it is placed:
        Top row:    9 5 8
        Middle row: 4 1 2
        Bottom row: 7 3 6

    This will assign a unique score each rotation of a board that is not 
    rotationally symmetrical, and we can select the one with the highest score 
    to store. This scoring method gives priority to the top left corner being
    empty.

