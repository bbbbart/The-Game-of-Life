import copy
import subprocess

def clear_terminal():
    subprocess.run("cls", shell=True)

def countNeighbors(y, x, grid):
    count = 0
    if y == 49 or y == 0 or x == 49 or x == 0:
        return -1
    else:
        if grid[y + 1][x] == "■":
            count+=1
        if grid[y][x + 1] == "■":
            count+=1
        if grid[y][x - 1] == "■":
            count+=1
        if grid[y - 1][x] == "■":
            count+=1
        if grid[y - 1][x - 1] == "■":
            count+=1
        if grid[y + 1][x + 1] == "■":
            count+=1
        if grid[y + 1][x - 1] == "■":
            count+=1
        if grid[y - 1][x + 1] == "■":
            count+=1
        return count

def updateGrid(grid):
    grid2 = copy.deepcopy(grid)
    for r, row in enumerate(grid):
        for c, element in enumerate(row):
            count = countNeighbors(r, c, grid)
            if count == -1:
                grid2[r][c] = "X"
            if 0 <= count <= 1:
                grid2[r][c] = "."
            if count > 3:
                grid2[r][c] = "."
            if element == "■" and 2 <= count <=3:
                grid2[r][c] = "■"
            if element == "." and count == 3:
                grid2[r][c] = "■"
    return grid2