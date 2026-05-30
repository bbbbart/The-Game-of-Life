grid = [["." for y in range(30)] for x in range (30)]

grid[15][16] = "■"
grid[15][17] = "■"
grid[14][15] = "■"

def countNeighbors(y, x):
    count = 0
    if y == 30 or y == 0 or x == 30 or x == 0:
        return -1
    else:
        if grid[y+1][x] == "■":
            count+=1
        if grid[y][x+1] == "■":
            count+=1
        if grid[y][x-1] == "■":
            count+=1
        if grid[y-1][x] == "■":
            count+=1
        return count
    
print(countNeighbors(15, 16))
for row in grid:
    print(" ".join(row))