import time
import copy
import subprocess
import random

def clear_terminal():
    subprocess.run("cls", shell=True)

def countNeighbors(y, x):
    count = 0
    if y == 49 or y == 0 or x == 49 or x == 0:
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

def updateGrid(grid):
    grid2 = copy.deepcopy(grid)
    for r, row in enumerate(grid):
        for c, element in enumerate(row):
            count = countNeighbors(r, c)
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

continueSimulation = True
while continueSimulation:
    grid1 = [["." for y in range(50)] for x in range (50)]
    choice = input("Choose a simulation\n 1. Glider \n 2. Gosper Glider Gun \n 3. Pulsar \n 4. Pentadecathlon \n 5. Random Grid \n ")

    if choice == "1":
        grid1[26][24] = "■"
        grid1[26][23] = "■"
        grid1[27][23] = "■"
        grid1[28][22] = "■"
        grid1[28][25] = "■"

    if choice == "2":
        grid1[5][1] = "■"
        grid1[5][2] = "■"
        grid1[6][1] = "■"
        grid1[6][2] = "■"
        grid1[3][13] = "■"
        grid1[3][14] = "■"
        grid1[4][12] = "■"
        grid1[4][16] = "■"
        grid1[5][11] = "■"
        grid1[5][17] = "■"
        grid1[6][11] = "■"
        grid1[6][15] = "■"
        grid1[6][17] = "■"
        grid1[6][18] = "■"
        grid1[7][11] = "■"
        grid1[7][17] = "■"
        grid1[8][12] = "■"
        grid1[8][16] = "■"
        grid1[9][13] = "■"
        grid1[9][14] = "■"
        grid1[1][25] = "■"
        grid1[2][23] = "■"
        grid1[2][25] = "■"
        grid1[3][21] = "■"
        grid1[3][22] = "■"
        grid1[4][21] = "■"
        grid1[4][22] = "■"
        grid1[5][21] = "■"
        grid1[5][22] = "■"
        grid1[6][23] = "■"
        grid1[6][25] = "■"
        grid1[7][25] = "■"
        grid1[3][35] = "■"
        grid1[3][36] = "■"
        grid1[4][35] = "■"
        grid1[4][36] = "■"

    if choice == "3":
        grid1[23][24] = "■"
        grid1[22][24] = "■"
        grid1[21][24] = "■"
        grid1[23][26] = "■"
        grid1[22][26] = "■"
        grid1[21][26] = "■"
        grid1[27][24] = "■"
        grid1[28][24] = "■"
        grid1[29][24] = "■"
        grid1[27][26] = "■"
        grid1[28][26] = "■"
        grid1[29][26] = "■"
        grid1[24][23] = "■"
        grid1[24][22] = "■"
        grid1[24][21] = "■"
        grid1[26][23] = "■"
        grid1[26][22] = "■"
        grid1[26][21] = "■"
        grid1[24][27] = "■"
        grid1[24][28] = "■"
        grid1[24][29] = "■"
        grid1[26][27] = "■"
        grid1[26][28] = "■"
        grid1[26][29] = "■"
        grid1[19][23] = "■"
        grid1[19][22] = "■"
        grid1[19][21] = "■"
        grid1[19][27] = "■"
        grid1[19][28] = "■"
        grid1[19][29] = "■"
        grid1[31][23] = "■"
        grid1[31][22] = "■"
        grid1[31][21] = "■"
        grid1[31][27] = "■"
        grid1[31][28] = "■"
        grid1[31][29] = "■"
        grid1[23][31] = "■"
        grid1[22][31] = "■"
        grid1[21][31] = "■"
        grid1[27][31] = "■"
        grid1[28][31] = "■"
        grid1[29][31] = "■"
        grid1[23][19] = "■"
        grid1[22][19] = "■"
        grid1[21][19] = "■"
        grid1[27][19] = "■"
        grid1[28][19] = "■"
        grid1[29][19] = "■"

    if choice == "4":
        grid1[25][21] = "■"
        grid1[25][22] = "■"
        grid1[25][24] = "■"
        grid1[25][25] = "■"
        grid1[25][26] = "■"
        grid1[25][27] = "■"
        grid1[25][29] = "■"
        grid1[25][30] = "■"
        grid1[24][23] = "■"
        grid1[26][23] = "■"
        grid1[24][28] = "■"
        grid1[26][28] = "■"

    if choice == "5":
        for r, row in enumerate(grid1):
            for c, element in enumerate(row):
                if random.random() <= 0.2:
                    grid1[r][c] = "■"

    for r, row in enumerate(grid1):
        for c, element in enumerate(row):
            if r == 0 or r == 49 or c == 0 or c == 49:
                grid1[r][c] = "X"

    generation = 0
    unpause = True
    while unpause:
        try: 
            while True:
                clear_terminal()
                generation+=1
                print("Click Cmd+C to Pause")
                print(f"Generation: {generation}\n")
                for row in grid1:
                    print(" ".join(row))
                time.sleep(0.5)
                grid1 = updateGrid(grid1)
        except KeyboardInterrupt:
            choice = input("SIMULATION PAUSED \n 1. Unpause \n 2. Return to Menu \n 3. Quit \n")
            if choice == "2":
                unpause = False
            if choice == "3":
                unpause = False
                continueSimulation = False
    clear_terminal()