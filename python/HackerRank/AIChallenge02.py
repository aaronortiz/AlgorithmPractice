#!/usr/bin/python

# --------------------------------------------------------------------------------------
def princessCoordsGet(n, grid):

    row = 0
    result = grid[row].find("p")

    while result == -1 and row < n:
        row += 1
        result = grid[row].find("p")

    if row < n:
        return {"y": row, "x": result}
    else:
        return {}


# --------------------------------------------------------------------------------------
def getVDirection(pLoc, botLoc):
    if pLoc["y"] == botLoc["y"]:
        return "NONE"
    elif pLoc["y"] < botLoc["y"]:
        return "UP"
    else:
        return "DOWN"


# --------------------------------------------------------------------------------------
def getHDirection(pLoc, botLoc):
    if pLoc["x"] == botLoc["x"]:
        return "NONE"
    elif pLoc["x"] < botLoc["x"]:
        return "LEFT"
    else:
        return "RIGHT"


# --------------------------------------------------------------------------------------
def nextMove(n, r, c, grid):
    pLoc = princessCoordsGet(n, grid)
    botLoc = {"y": r, "x": c}
    vDir = getVDirection(pLoc, botLoc)
    hDir = getHDirection(pLoc, botLoc)

    if abs(botLoc["x"] - pLoc["x"]) > abs(botLoc["y"] - pLoc["y"]):
        return hDir
    else:
        return vDir


# --------------------------------------------------------------------------------------
n = int(input())
r, c = [int(i) for i in input().strip().split()]
grid = []
for i in range(0, n):
    grid.append(input())

print(nextMove(n, r, c, grid))
