import random

def glider(grid):
    grid = grid
    grid[26][24] = "■"
    grid[26][23] = "■"
    grid[27][23] = "■"
    grid[28][22] = "■"
    grid[28][25] = "■"
    
    return grid

def gliderGun(grid):
    grid = grid
    grid[5][1] = "■"
    grid[5][2] = "■"
    grid[6][1] = "■"
    grid[6][2] = "■"
    grid[3][13] = "■"
    grid[3][14] = "■"
    grid[4][12] = "■"
    grid[4][16] = "■"
    grid[5][11] = "■"
    grid[5][17] = "■"
    grid[6][11] = "■"
    grid[6][15] = "■"
    grid[6][17] = "■"
    grid[6][18] = "■"
    grid[7][11] = "■"
    grid[7][17] = "■"
    grid[8][12] = "■"
    grid[8][16] = "■"
    grid[9][13] = "■"
    grid[9][14] = "■"
    grid[1][25] = "■"
    grid[2][23] = "■"
    grid[2][25] = "■"
    grid[3][21] = "■"
    grid[3][22] = "■"
    grid[4][21] = "■"
    grid[4][22] = "■"
    grid[5][21] = "■"
    grid[5][22] = "■"
    grid[6][23] = "■"
    grid[6][25] = "■"
    grid[7][25] = "■"
    grid[3][35] = "■"
    grid[3][36] = "■"
    grid[4][35] = "■"
    grid[4][36] = "■"
    
    return grid

def pulsar(grid):
    grid = grid
    grid[23][24] = "■"
    grid[22][24] = "■"
    grid[21][24] = "■"
    grid[23][26] = "■"
    grid[22][26] = "■"
    grid[21][26] = "■"
    grid[27][24] = "■"
    grid[28][24] = "■"
    grid[29][24] = "■"
    grid[27][26] = "■"
    grid[28][26] = "■"
    grid[29][26] = "■"
    grid[24][23] = "■"
    grid[24][22] = "■"
    grid[24][21] = "■"
    grid[26][23] = "■"
    grid[26][22] = "■"
    grid[26][21] = "■"
    grid[24][27] = "■"
    grid[24][28] = "■"
    grid[24][29] = "■"
    grid[26][27] = "■"
    grid[26][28] = "■"
    grid[26][29] = "■"
    grid[19][23] = "■"
    grid[19][22] = "■"
    grid[19][21] = "■"
    grid[19][27] = "■"
    grid[19][28] = "■"
    grid[19][29] = "■"
    grid[31][23] = "■"
    grid[31][22] = "■"
    grid[31][21] = "■"
    grid[31][27] = "■"
    grid[31][28] = "■"
    grid[31][29] = "■"
    grid[23][31] = "■"
    grid[22][31] = "■"
    grid[21][31] = "■"
    grid[27][31] = "■"
    grid[28][31] = "■"
    grid[29][31] = "■"
    grid[23][19] = "■"
    grid[22][19] = "■"
    grid[21][19] = "■"
    grid[27][19] = "■"
    grid[28][19] = "■"
    grid[29][19] = "■"
    
    return grid

def Pentadecathlon(grid):
    grid = grid
    grid[25][21] = "■"
    grid[25][22] = "■"
    grid[25][24] = "■"
    grid[25][25] = "■"
    grid[25][26] = "■"
    grid[25][27] = "■"
    grid[25][29] = "■"
    grid[25][30] = "■"
    grid[24][23] = "■"
    grid[26][23] = "■"
    grid[24][28] = "■"
    grid[26][28] = "■"

    return grid

def randomGrid(grid):
    grid = grid
    for r, row in enumerate(grid):
            for c, element in enumerate(row):
                if random.random() <= 0.2:
                    grid[r][c] = "■"
    return grid
