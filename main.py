import time
import grid
import patterns

continueSimulation = True
while continueSimulation:
    grid1 = [["." for y in range(50)] for x in range (50)]
    generation = 0
    unpause = True

    choice = input("Choose a simulation\n 1. Glider \n 2. Gosper Glider Gun \n 3. Pulsar \n 4. Pentadecathlon \n 5. Random Grid \n ")
    if choice == "1":
        grid1 = patterns.glider(grid1)
    if choice == "2":
        grid1 = patterns.gliderGun(grid1)
    if choice == "3":
        grid1 = patterns.pulsar(grid1)
    if choice == "4":
        grid1 = patterns.Pentadecathlon(grid1)
    if choice == "5":
        grid1 = patterns.randomGrid(grid1)

    for r, row in enumerate(grid1):
        for c, element in enumerate(row):
            if r == 0 or r == 49 or c == 0 or c == 49:
                grid1[r][c] = "X"

    while unpause:
        try: 
            while True:
                grid.clear_terminal()               
                generation+=1
                print("Click Ctrl+C to Pause")
                print(f"Generation: {generation}\n")
                for row in grid1:
                    print(" ".join(row))
                time.sleep(0.75)
                grid1 = grid.updateGrid(grid1)
        except KeyboardInterrupt:
            choice = input("SIMULATION PAUSED \n 1. Unpause \n 2. Return to Menu \n 3. Quit \n")
            if choice == "2":
                unpause = False
            if choice == "3":
                unpause = False
                continueSimulation = False
    grid.clear_terminal()