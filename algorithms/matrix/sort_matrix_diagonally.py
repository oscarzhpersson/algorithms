"""
Given a m * n matrix mat of integers,
sort it diagonally in ascending order
from the top-left to the bottom-right
then return the sorted array.

mat = [
    [3,3,1,1],
    [2,2,1,2],
    [1,1,1,2]
]

Should return:
[
    [1,1,1,1],
    [1,2,2,2],
    [1,2,3,3]
]
"""

from heapq import heappush, heappop
from typing import List

flags = {
    "0" : 0, #if
    "1" : 0, #if
    "2" : 0, #for
    "3" : 0, #if
    "4" : 0, #while
    "5" : 0, #while
    "6" : 0, #else
    "7" : 0, #while
    "8" : 0, #while
}

# INPUT ARGUMENTS
# h - heap
# mat - matrix
# row - row of matrix
# col - column of matrix
# flagID - flags index
# flag - sets while conditional

def sort_diagonal(h, mat, row, col, flagID):
    while h:
        flags[flagID] += 1
        ele = heappop(h)
        mat[row][col] = ele
        row += 1
        col += 1

def traverse(h, mat, row, col, flagID, flag):
    if flag: 
        while row < len(mat) and col < len(mat[0]):
            row, col = traverse_diagonal(h, mat, row, col, flagID)
    else:
        while row < len(mat):
            row, col = traverse_diagonal(h, mat, row, col, flagID)
            
def traverse_diagonal(h, mat, row, col, flagID):
    flags[flagID] += 1
    heappush(h, (mat[row][col]))
    row += 1
    col += 1
    return row, col

def sort_diagonally(mat: List[List[int]]) -> List[List[int]]:
    # If the input is a vector, return the vector
    # This if statement is never tested, a vector is never given 
    # as input in the unit test for this function
    if len(mat) == 1:
        flags["0"] += 1
        return mat, flags
    
    if len(mat[0]) == 1:
        flags["1"] += 1
        return mat, flags

    # Rows + columns - 1
    # The -1 helps you to not repeat a column
    for i in range(len(mat)+len(mat[0])-1):
        flags["2"] += 1
        # Process the rows
        if i+1 < len(mat):
            flags["3"] += 1

            # Initialize heap, set row and column
            h = []
            row = len(mat)-(i+1)
            col = 0

            # Traverse diagonally, and add the values to the heap
            traverse(h, mat, row, col, "4", False)
            
            # Sort the diagonal
            row = len(mat)-(i+1)
            col = 0
            sort_diagonal(h, mat, row, col, "5")

        else:
            flags["6"] += 1
            # Process the columns

            # Initialize heap, row and column
            h = []
            row = 0
            col = i - (len(mat)-1)

            # Traverse Diagonally
            traverse(h, mat, row, col, "7", True)

            # Sort the diagonal
            row = 0
            col = i - (len(mat)-1)
            sort_diagonal(h, mat, row, col, "8")
    
    # Return the updated matrix
    return mat, flags