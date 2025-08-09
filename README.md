# Conway's Game of Life 
A terminal version of Conway's Game of Life in Python. Made by Santiago Padron. Summer 2025

This project was inspired by [Robert Heaton's tutorial](https://robertheaton.com/2018/07/20/project-2-game-of-life/). I took his advice on the implementation of the game, but also made it mine by adding some features, like a main menu.

## Running the game
This project uses the `art` library for ASCII art and the `getkey` library. Make sure to download those libraries.
```
pip install art
pip install getkey
```

Then, to run the game, simply run the `game.py` file
```
python game.py
```
The game will greet you with a main menu, and you can either press `x` to start the game with a randomized starting board(also called "soup") or press `q` to quit the game. Once the game is started, I have yet to found a nice solution, but the only to way to quit the game is by pressing `Ctrl+C`

## Implementation
For those who don't know Conway's Game of Life, here is how it works in a nutshell:

The universe is composed of a grid of cells, which state can either be `alive (1)` or `dead (0)`. The starting board -- in my case generated randomly -- is then updated periodically according to the following simple rules:
- A live (1) cell with 0 or 1 neighbors dies (0)
- A live (1) cell with 2 or 3 neighbors stays alive (1)
- A live (1) cell with more than 3 neighbors dies (0)
- A dead (0) cell with exactly 3 neighbors lives (1)
And this game runs forever. There is no winning or losing, simply watching the cells reproduce and live this Life.

To implement this game, the board is represented as a 2D array of 0s and 1s, representing the cell states. Then, each following state is calculated based on the rules, and we render the board to the terminal periodically.

## What I learned
- Using `pip` to install external librairies in my projects
- Using `venv` in python to isolate libraries
- Separating code in functions and having well structured and clean code

## TODO
- [x] More testings to confirm that the game functions
- [x] Make the game run forever and update
- [x] Include os module to auto-size to terminal window
- [ ] Make main menu and pause/quit button (IN PROGRESS)
- [ ] Support to load-from-file
