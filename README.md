# Conway's Game of Life

<img width="709" height="914" alt="image" src="https://github.com/user-attachments/assets/07a3c4bc-5447-4474-9455-fdb41bdf3919" />

This is my attempt at coding Conway's Game of Life as a beginner challenge for learning Python and GitHub for the first time.

## Warning
Those with a history of photosensitive epilepsy should avoid running this program due to the terminal being prone to flickering while running.

## Features

- Terminal-based 50x50 Conway's Game of Life simulation
- 5 pattern presets
- Generation counter
- Pause menu (Ctrl+C)

### Pattern Presets
- Glider
- Gosper Glider Gun
- Pulsar
- Pentadecathlon
- Random Grid


#### Glider:

A repeating pattern that moves across the grid diagonally. 


#### Gosper Glider Gun: 

A pattern that continuously creates new gliders. 


#### Pulsar:

A repeating pattern that pulsates in a star-like pattern 


#### Pentadecathlon: 

A repeating pattern that oscillates through multiple states. 


#### Random Grid: 

Creates a grid where each cell has a 20% chance to begin in a live state. 

### Rules

Each cell follows these 4 rules: 

1.  Any live cell with fewer than 2 neighbors dies
2.  Any live cell with more than 3 neighbors dies
3.  Any live cell with 2 or 3 neighbors survives
4.  Any dead cell that has exactly 3 neighbors becomes alive

### User Inputs

When running the simulation, you begin with an option to choose a preset, which can be done by entering the appropriate number into the terminal. A simulation can be paused by pressing Ctrl+C, which then gives the options of unpausing, returning to selection menu, and quitting the program.

## Requirements and Running

This program uses Python 3.14 or newer

See release 1.0.0 for link to zip download.

Clone or download repository and run:
`py main.py`

## More Info
[Conway's Game of Life on Wikipedia](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life)

[Official Game](https://playgameoflife.com/)

     
