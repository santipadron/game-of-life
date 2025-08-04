## Conway's Game of Life
## By Santiago Padron

import random as r

def dead_state(width, height):
    board = []

    for j in range(height):
        board.append([0] * width)

    return board


def rand_state(width, height):
    board = dead_state(width, height)

    for i in range(height):
        for j in range(width):
            num = r.random()
            if num > 0.9:
                board[i][j] = 1
            else:
                board[i][j] = 0

    return board


def render(board_state):
    print(" " + "-"*len(board_state[0])*2 + " ")

    for row in board_state:
        line = "|"
        for col in row:
            if (col == 1):
                line += "\u2588" * 2
            else:
                line += "  "
        line += "|"
        print(line)

    print(" " + "-"*len(board_state[0])*2 + " ")


def next_board_state(board_state):
    """
    Calculates next board state based on Conway's Life rules:
        - A live (1) cell with 0 or 1 neighbors dies (0)
        - A live (1) cell with 2 or 3 neighbors stays alive (1)
        - A live (1) cell with more than 3 neighbors dies (0)
        - A dead (0) cell with exactly 3 neighbors lives (1)
    
    Input: board_state: [[int]]
    Output: updated_board_state: [[int]]
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

            # Count neighbors
            neighbor_count = count_neighbors(i, j)

            # Check rules
            if (curr_state == 1) and (neighbor_count <= 1 or neighbor_count > 3):
                next_state = 0
            elif (curr_state == 1) and (neighbor_count == 2 or neighbor_count == 3):
                next_state = 1
            elif (curr_state == 0) and (neighbor_count == 3):
                next_state = 1

            #Update board
            updated_board_state[i][j] = next_state

    return updated_board_state


# testing
if __name__ == "__main__":
    state_d = dead_state(50,25)
    state_r = rand_state(50, 25)

    print(state_d)
    print(state_r)
    print('\u2588')
    render(state_d)
    render(state_r)

