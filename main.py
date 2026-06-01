import time
import grid
import patterns

continueSimulation = True
gridsize = 50

while continueSimulation: ## checks if user quits simulation or returns to menu
    grid1 = [["." for y in range(gridsize)] for x in range (gridsize)]
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
        grid1 = patterns.pentadecathlon(grid1)
    if choice == "5":
        grid1 = patterns.randomGrid(grid1)

    for r, row in enumerate(grid1):  ##creates grid border
        for c, element in enumerate(row):
            if r == 0 or r == gridsize-1 or c == 0 or c == gridsize-1:
                grid1[r][c] = "X"

    while unpause: ## checks if user unpauses
        try: 
            while True:
                grid.clear_terminal()               
                generation+=1
                print("Click Ctrl+C to Pause")
                print(f"Generation: {generation}\n")
                for row in grid1:
                    print(" ".join(row))
                time.sleep(0.5)
                grid1 = grid.updateGrid(grid1)
        except KeyboardInterrupt:
            choice = input("SIMULATION PAUSED \n 1. Unpause \n 2. Return to Menu \n 3. Quit \n")
            if choice == "2":
                unpause = False
            if choice == "3":
                unpause = False
                continueSimulation = False
    grid.clear_terminal()