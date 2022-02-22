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
    "1" : 0, #for
    "2" : 0, #if
    "3" : 0, #while
    "4" : 0, #while
    "5" : 0, #else
    "6" : 0, #while
    "7" : 0, #while
}

def sort_diagonally(mat: List[List[int]]) -> List[List[int]]:

    # If the input is a vector, return the vector
    # This if statement is never tested, a vector is never given 
    # as input in the unit test for this function
    if len(mat) == 1 or len(mat[0]) == 1:
        flags["0"] += 1
        return mat

    # Rows + columns - 1
    # The -1 helps you to not repeat a column
    for i in range(len(mat)+len(mat[0])-1):
        flags["1"] += 1
        # Process the rows
        if i+1 < len(mat):
            flags["2"] += 1
            # Initialize heap, set row and column
            h = []
            row = len(mat)-(i+1)
            col = 0

            # Traverse diagonally, and add the values to the heap
            while row < len(mat):
                flags["3"] += 1
                heappush(h, (mat[row][col]))
                row += 1
                col += 1

            # Sort the diagonal
            row = len(mat)-(i+1)
            col = 0
            while h:
                flags["4"] += 1
                ele = heappop(h)
                mat[row][col] = ele
                row += 1
                col += 1
        else:
            flags["5"] += 1
            # Process the columns
            # Initialize heap, row and column
            h = []
            row = 0
            col = i - (len(mat)-1)

            # Traverse Diagonally
            while col < len(mat[0]) and row < len(mat):
                flags["6"] += 1
                heappush(h, (mat[row][col]))
                row += 1
                col += 1

            # Sort the diagonal
            row = 0
            col = i - (len(mat)-1)
            while h:
                flags["7"] += 1
                ele = heappop(h)
                mat[row][col] = ele
                row += 1
                col += 1

    print("function sort_diagonally")
    for key,value in flags.items():
        print(key + ": " + str(value))

    for key in flags:
        flags[key] = 0
    
    # Return the updated matrix
    return mat
