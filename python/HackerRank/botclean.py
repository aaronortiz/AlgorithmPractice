#!/usr/bin/python

# Head ends here

import random


def scoreUp(row, board):
    score = 0
    for r in range(row):
        for c in range(len(board[0])):
            if board[r][c] == "d":
                score += 1
    return score


def scoreDown(row, board):
    score = 0
    for r in range(row + 1, len(board)):
        for c in range(len(board[0])):
            if board[r][c] == "d":
                score += 1
    return score


def scoreLeft(col, board):
    score = 0
    for r in range(len(board)):
        for c in range(col):
            if board[r][c] == "d":
                score += 1
    return score


def scoreRight(col, board):
    score = 0
    for r in range(len(board)):
        for c in range(col + 1, len(board[0])):
            if board[r][c] == "d":
                score += 1
    return score


def moveFromMaxScore(uScore, dScore, lScore, rScore):

    if uScore == 0 and dScore == 0 and lScore == 0 and rScore == 0:
        return ""
    elif uScore > 0 and uScore > max(dScore, lScore, rScore):
        return "UP"
    elif dScore > 0 and dScore > max(uScore, lScore, rScore):
        return "DOWN"
    elif lScore > 0 and lScore > max(uScore, dScore, rScore):
        return "LEFT"
    elif rScore > 0 and rScore > max(uScore, dScore, lScore):
        return "RIGHT"
    elif lScore > 0:
        return "LEFT"
    elif rScore > 0:
        return "RIGHT"
    elif uScore > 0:
        return "UP"
    elif dScore > 0:
        return "DOWN"


def moveToAdjacentDirt(posr, posc, board):

    if posc < len(board[0]) - 1 and board[posr][posc + 1] == "d":
        return "RIGHT"
    elif posc > 0 and board[posr][posc - 1] == "d":
        return "LEFT"
    elif posr < len(board) - 1 and board[posr + 1][posc] == "d":
        return "DOWN"
    elif posr > 0 and board[posr - 1][posc] == "d":
        return "UP"
    else:
        return ""


def moveToDiagonalDirt(posr, posc, board):
    if (  # Can't move diagonally DOWN + RIGHT
        posr < len(board) - 1
        and posc < len(board[0]) - 1
        and board[posr + 1][posc + 1] == "d"
    ):
        return "RIGHT"
    elif (  # Can't move diagonally UP + RIGHT
        posr > 0 and posc < len(board[0]) - 1 and board[posr - 1][posc + 1] == "d"
    ):
        return "RIGHT"
    elif (  # Can't move diagonally DOWN + LEFT
        posr < len(board) - 1 and posc > 0 and board[posr + 1][posc - 1] == "d"
    ):
        return "LEFT"
    elif (  # Can't move diagonally UP + LEFT
        posr > 0 and posc > 0 and board[posr - 1][posc - 1] == "d"
    ):
        return "LEFT"
    else:
        return ""


def next_move(posr, posc, board):

    uScore = 0
    dScore = 0
    lScore = 0
    rScore = 0
    possibleMoves = []

    if board[posr][posc] == "d":
        print("CLEAN")
    else:
        move = moveToAdjacentDirt(posr, posc, board)
        if len(move) > 0:
            print(move)
        else:
            move = moveToDiagonalDirt(posr, posc, board)
            if len(move) > 0:
                print(move)
            else:
                if posr > 0:
                    uScore = scoreUp(posr, board)
                    possibleMoves.append("UP")
                if posr < len(board) - 1:
                    dScore = scoreDown(posr, board)
                    possibleMoves.append("DOWN")
                if posc > 0:
                    lScore = scoreLeft(posc, board)
                    possibleMoves.append("LEFT")
                if posc < len(board[0]) - 1:
                    rScore = scoreRight(posc, board)
                    possibleMoves.append("RIGHT")

                move = moveFromMaxScore(uScore, dScore, lScore, rScore)
                if len(move) > 0:
                    print(move)
                else:
                    print(random.choice(possibleMoves))


# Tail starts here

if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)
    """
    next_move(
        1,
        4,
        [
            ["-", "-", "-", "-", "-"],
            ["d", "-", "-", "-", "b"],
            ["d", "-", "-", "-", "-"],
            ["d", "-", "-", "-", "-"],
            ["d", "-", "-", "-", "d"],
        ],
    )
    """
