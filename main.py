import time

grid1 = [["." for y in range(30)] for x in range (30)]

grid1[15][15] = "■"
grid1[15][16] = "■"
grid1[15][17] = "■"
grid1[16][17] = "■"
grid1[17][16] = "■"

def countNeighbors(y, x):
    count = 0
    if y == 30 or y == 0 or x == 30 or x == 0:
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
    grid2 = [["." for y in range(30)] for x in range (30)]
    r = -1
    c = -1
    for row in g:
        r+=1
        for element in g:
            c+=1
            count = countNeighbors(r, c)
            if count <= 1:
                grid2[r][c] = "."
            elif count >= 4:
                grid2[r][c] = "."
            elif element == "■" and 2 <= count <=3:
                grid2[r][c] = "■"
    return grid2

for i in range(10):
    for row in grid1:
        print(" ".join(row))
    time.sleep(1)
    print("\033[H\033[2J", end="")
    grid1 = updateGrid(grid1)