import time
import copy

grid1 = [["." for y in range(30)] for x in range (30)]

grid1[3][16] = "■"
grid1[3][17] = "■"
grid1[3][18] = "■"
grid1[4][18] = "■"
grid1[5][17] = "■"


def countNeighbors(y, x):
    count = 0
    if y == 29 or y == 0 or x == 29 or x == 0:
        return -1
    else:
        if grid1[y + 1][x] == "■":
            count+=1
        if grid1[y][x + 1] == "■":
            count+=1
        if grid1[y][x - 1] == "■":
            count+=1
        if grid1[y - 1][x] == "■":
            count+=1
        if grid1[y - 1][x - 1] == "■":
            count+=1
        if grid1[y + 1][x + 1] == "■":
            count+=1
        if grid1[y + 1][x - 1] == "■":
            count+=1
        if grid1[y - 1][x + 1] == "■":
            count+=1
        return count

def updateGrid(g):
    grid2 = copy.deepcopy(g)
    r = 0
    c = 0
    for row in g:
        for element in row:
            count = countNeighbors(r, c)
            if count <= 1:
                grid2[r][c] = "."
            if count > 3:
                grid2[r][c] = "."
            if element == "■" and 2 <= count <=3:
                grid2[r][c] = "■"
            if element == "." and count == 3:
                grid2[r][c] = "■"
            c+=1
        c = 0
        r+=1
    return grid2

for i in range(10):
    for row in grid1:
        print(" ".join(row))
    print("\n")
    time.sleep(1)
    grid1 = updateGrid(grid1)