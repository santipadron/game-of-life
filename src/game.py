## Conway's Game of Life
## By Santiago Padron

import random as r
import time
import os
import art
import getkey 


def dead_state(width, height):
    """Generates a blank starting board based on the dimensions"""
    board = []

    for j in range(height):
        board.append([0] * width)

    return board


def rand_state(width, height):
    """Generates a random starting board based on the dimensions"""
    THRESHOLD = 0.9
    board = dead_state(width, height)

    for i in range(height):
        for j in range(width):
            num = r.random()
            if num > THRESHOLD:
                board[i][j] = 1
            else:
                board[i][j] = 0

    return board


def render(board_state):
    """
    Renders the board state to the terminal. Uses two unicode characters U+2588 to display a live cell
    and two spaces for a dead cell

    Input: Current board_state: List(List(int))
    Output: void
    """
    for row in board_state:
        line = ""
        for col in row:
            if (col == 1):
                line += "\u2588" * 2
            else:
                line += "  "
        print(line)


def next_board_state(board_state):
    """
    Calculates next board state based on Conway's Life rules:
        - A live (1) cell with 0 or 1 neighbors dies (0)
        - A live (1) cell with 2 or 3 neighbors stays alive (1)
        - A live (1) cell with more than 3 neighbors dies (0)
        - A dead (0) cell with exactly 3 neighbors lives (1)
    
    Input: board_state: List(List(int)) 
    Output: updated_board_state: List(List(int))
    """
    width = len(board_state[0])
    height = len(board_state)
    updated_board_state = dead_state(width, height)
    
    # Helper method to count neighbors
    def count_neighbors(i, j):
        count = 0
        for m in range(i-1, i+2):
            for n in range(j-1, j+2):
                if m == i and n == j: continue
                
                if m < 0 or n < 0 or m >= height or n >= width: continue

                count += board_state[m][n]
        
        return count
    
    # Calculate updated board
    for i in range(height):
        for j in range(width):
            neighbor_count = 0
            curr_state = board_state[i][j]
            next_state = 0

            neighbor_count = count_neighbors(i, j)

            # Check rules
            if (curr_state == 1) and (neighbor_count <= 1 or neighbor_count > 3):
                next_state = 0
            elif (curr_state == 1) and (neighbor_count == 2 or neighbor_count == 3):
                next_state = 1
            elif (curr_state == 0) and (neighbor_count == 3):
                next_state = 1

            updated_board_state[i][j] = next_state

    return updated_board_state


def main_menu(width, height):
    """Displays main menu and prompts player to start or quit the game"""
    art.lprint(width, 3, "*")
    art.tprint("Conway's Game of Life", "tarty3")
    art.lprint(width, 3, "*")
    print("Welcome to Conway's Game of Life. This is a simple, terminal version of the classic game.\nPress [X] to Start\nPress [Q] to Quit")


def play_game(width, height):
    """Plays the game by updating and rendering the board through each life cycle"""
    board = rand_state(width, height)

    while True:
        render(board)
        time.sleep(0.1)
        os.system("cls" if os.name == "nt" else "clear") # Clear terminal window for cleaner rendering
        board = next_board_state(board)



# run the game
if __name__ == "__main__":
    
    # Get the size of the terminal window
    width = int((os.get_terminal_size()[0])/2) # Since we render cells as either two filled
                                        # squares or two spaces, we half the usable width
    height = int(os.get_terminal_size()[1])

    main_menu(width*2, height)
    
    while True:
        key = getkey.getkey()

        if key == "x":
            play_game(width, height)
        elif key == "q": break


