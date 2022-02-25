"""
Write a function validSolution/ValidateSolution/valid_solution() that accepts a 2D array representing a Sudoku board, and returns true if it is a valid solution, or false otherwise. The cells of the sudoku board may also contain 0's, which will represent empty cells. Boards containing one or more zeroes are considered to be invalid solutions.
The board is always 9 cells by 9 cells, and every cell only contains integers from 0 to 9.

(More info at: http://en.wikipedia.org/wiki/Sudoku)
"""

flags = {
    "0" : 0, 
    "1" : 0, 
    "2" : 0, 
    "3**" : 0, # Test should be added for this flag
    "4" : 0, 
    "5**" : 0, # Test should be added for this flag
    "6" : 0, 
    "7" : 0, 
    "8" : 0, 
    "9" : 0, 
    "10" : 0, 
    "11" : 0, 
    "12" : 0, 
    "13" : 0, 
    "14" : 0, 
    "15" : 0, 
    "16" : 0, 
    "17" : 0, 
    "18" : 0, 
    "19" : 0, 
    "20" : 0, 
    "21" : 0, 
    "22" : 0, 
    "23" : 0, 
    "24" : 0, 
    "25" : 0, 
    "26" : 0, 
}

# Using dict/hash-table
from collections import defaultdict
def valid_solution_hashtable(board):
    for i in range(len(board)):
        # flags["0"] += 1
        dict_row = defaultdict(int)
        dict_col = defaultdict(int)
        for j in range(len(board[0])):
            # flags["1"] += 1
            value_row = board[i][j]
            value_col = board[j][i]
            if not value_row or value_col == 0:
                # flags["2"] += 1
                return False, flags
            if value_row in dict_row:
                flags["3**"] += 1
                return False, flags
            else:
                # flags["4"] += 1
                dict_row[value_row] += 1

            if value_col in dict_col:
                flags["5**"] += 1
                return False, flags
            else:
                # flags["6"] += 1
                dict_col[value_col] += 1

    for i in range(3):
        # flags["7"] += 1
        for j in range(3):
            # flags["8"] += 1
            grid_add = 0
            for k in range(3):
                # flags["9"] += 1
                for l in range(3):
                    # flags["10"] += 1
                    grid_add += board[i*3+k][j*3+l]
            if grid_add != 45:
                # flags["11"] += 1
                return False, flags
    return True, flags


# Without hash-table/dict
def valid_solution(board):
    correct = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # check rows
    for row in board:
        # flags["12"] += 1
        if sorted(row) != correct:
            # flags["13"] += 1
            return False, flags

    # check columns
    for column in zip(*board):
        # flags["14"] += 1
        if sorted(column) != correct:
            # flags["15"] += 1
            return False, flags

    # check regions
    for i in range(3):
        # flags["16"] += 1
        for j in range(3):
            # flags["17"] += 1
            region = []
            for line in board[i*3:(i+1)*3]:
                # flags["18"] += 1
                region += line[j*3:(j+1)*3]

            if sorted(region) != correct:
                # flags["19"] += 1
                return False, flags

    # if everything correct
    return True, flags


# Using set
def valid_solution_set (board):
    valid = set(range(1, 10))

    for row in board:
        # flags["20"] += 1
        if set(row) != valid:
            flags["21"] += 1
            return False, flags

    for col in [[row[i] for row in board] for i in range(9)]:
        # flags["22"] += 1
        if set(col) != valid:
            flags["23"] += 1
            return False, flags

    for x in range(3):
        # flags["24"] += 1
        for y in range(3):
            flags["25"] += 1
            if set(sum([row[x*3:(x+1)*3] for row in board[y*3:(y+1)*3]], [])) != valid:
                # flags["26"] += 1
                return False, flags

    return True, flags
