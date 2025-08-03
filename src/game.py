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


# testing

state_d = dead_state(20,30)
state_r = rand_state(20, 30)

print(state_d)
print(state_r)
print('\u2588')
render(state_d)
render(state_r)

