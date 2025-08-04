## Conway's Game of Life Unit Tests
## By Santiago Padron

import game as g

def header(num):
    print("-"*10 + "TEST #" + str(num) + "-"*10)

def test_print(num, initial, expected):
    header(num)
    actual = g.next_board_state(initial)
    
    if actual == expected:
        print("Passed Test #" + str(num))
    else:
        print("Test #" + str(num) + " failed")
        print("initial board:")
        g.render(initial)
        print("expected board:")
        g.render(expected)
        print("actual result:")
        g.render(actual)

    print("-"*27)

if __name__ == "__main__":
    # test 1: dead cells with no live neighbors
    init_st1 = [
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]
    exp_st1 = [
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]
    test_print(1, init_st1, exp_st1)

    # test 2: dead cells with exactly 3 neighbors
    init_st2 = [
        [0,0,1],
        [0,1,1],
        [0,0,0]
    ]
    exp_st2 = [
        [0,1,1],
        [0,1,1],
        [0,0,0]
    ]
    test_print(2, init_st2, exp_st2)
    
    # test 3: live cells with more than 3 neighbors
    init_st3 = [
        [1,1,1],
        [1,1,1],
        [1,1,1]
    ]
    exp_st3 = [
        [1,0,1],
        [0,0,0],
        [1,0,1]
    ]
    test_print(3, init_st3, exp_st3)

    # test 4: multiple rules at once
    init_st4 = [
        [1,0,1],
        [0,1,1],
        [1,0,1]
    ]
    exp_st4 = [
        [0,0,1],
        [1,0,1],
        [0,0,1]
    ]
    test_print(4, init_st4, exp_st4)

