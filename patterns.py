import random

def printPattern(grid, pattern): 
    for r, c in pattern:
        grid[r][c] = "■"
    return grid

def glider(grid):
    glider = ((26, 24), (26, 23), (26, 22), 
              (27, 22), (28, 23))
    return printPattern(grid, glider)

def gliderGun(grid):
    gliderGun = ((5, 1), (5, 2), (6, 1), 
                 (6, 2), (3, 13), (3, 14), 
                 (4, 12), (4, 16), (5, 11), 
                 (5, 17), (6, 11), (6, 15), 
                 (6, 17), (6, 18), (7, 11), 
                 (7, 17), (8, 12), (8, 16), 
                 (9, 13), (9, 14), (1, 25), 
                 (2, 23), (2, 25), (3, 21), 
                 (3, 22), (4, 21), (4, 22), 
                 (5, 21), (5, 22), (6, 23), 
                 (6, 25), (7, 25), (3, 35), 
                 (3, 36), (4, 35), (4, 36)) 
    return printPattern(grid, gliderGun)

def pulsar(grid):
    pulsar = ((23, 24), (22, 24), (21, 24),
              (23, 26), (22, 26), (21, 26),
              (27, 24), (28, 24), (29, 24),
              (27, 26), (28, 26), (29, 26),
              (24, 23), (24, 22), (24, 21),
              (26, 23), (26, 22), (26, 21),
              (24, 27), (24, 28), (24, 29),
              (26, 27), (26, 28), (26, 29),
              (19, 23), (19, 22), (19, 21),
              (19, 27), (19, 28), (19, 29), 
              (31, 23), (31, 22), (31, 21),
              (31, 27), (31, 28), (31, 29),
              (23, 31), (22, 31), (21, 31), 
              (27, 31), (28, 31), (29, 31), 
              (23, 19), (22, 19), (21, 19),
              (27, 19), (28, 19), (29, 19))
    return printPattern(grid, pulsar)

def pentadecathlon(grid):
    pentadecathlon = ((24,21), (24,22), (24,24), 
                      (24,25), (24,26), (24,27), 
                      (24,29), (24,30), (23,23), 
                      (25,23), (23,28), (25,28))
    return printPattern(grid, pentadecathlon)

def randomGrid(grid):
    for r, row in enumerate(grid):
            for c in enumerate(row):
                if random.random() <= 0.2:
                    grid[r][c] = "■"
    return grid