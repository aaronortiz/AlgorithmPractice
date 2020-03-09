#!/usr/bin/python
import copy

# ---------------------------------------------
def princessCoordsGet(n, grid):

    # Assume princess is in top left corner
    pLoc = {"x": 0, "y": 0}

    # But if she isn't, try bottom left
    if grid[pLoc["y"]][pLoc["x"]].lower() != "p":
        pLoc["y"] = n - 1
    # Ditto for bottom left
    if grid[pLoc["y"]][pLoc["x"]].lower() != "p":
        pLoc["x"] = n - 1
    # Ditto for top right
    if grid[pLoc["y"]][pLoc["x"]].lower() != "p":
        pLoc["y"] = 0

    return pLoc


# ---------------------------------------------
def botCoordsGet(n):

    # Bot is in middle square by definition
    middle = (n - 1) / 2
    botLoc = {"x": middle, "y": middle}

    return botLoc


# ---------------------------------------------
def getVDirection(pLoc, botLoc):
    if pLoc["y"] < botLoc["y"]:
        return "UP"
    else:
        return "DOWN"


# ---------------------------------------------
def getHDirection(pLoc, botLoc):
    if pLoc["x"] < botLoc["x"]:
        return "LEFT"
    else:
        return "RIGHT"


# ---------------------------------------------
def displayPathtoPrincess(n, grid):

    pLoc = princessCoordsGet(n, grid)
    botLoc = botCoordsGet(n)
    vDir = getVDirection(pLoc, botLoc)
    hDir = getHDirection(pLoc, botLoc)

    curLoc = copy.deepcopy(botLoc)

    while (
        curLoc["x"] > 0
        and curLoc["x"] < n - 1
        and curLoc["y"] > 0
        and curLoc["y"] < n - 1
    ):
        print(vDir)
        print(hDir)

        if vDir == "UP":
            curLoc["y"] -= 1
        else:
            curLoc["y"] += 1

        if hDir == "LEFT":
            curLoc["x"] -= 1
        else:
            curLoc["x"] += 1

    return True


m = int(input())
grid = []
for i in range(0, m):
    grid.append(input().strip())

displayPathtoPrincess(m, grid)

