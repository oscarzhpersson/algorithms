from algorithms.bfs import (
    count_islands,
    maze_search,
    shortest_distance_from_all_buildings,
    ladder_length
)

import unittest

flag = [0]*6

class TestMazeSearch_Issue5(unittest.TestCase):
    
    def test_maze_search(self):
        grid_1 = [[1,0,1,1,1,1],[1,0,1,0,1,0],[1,0,1,0,1,1],[1,1,1,0,1,1]]
        self.assertEqual(14, maze_search(grid_1, flag))

        grid_2 = [[1,0,0],[0,1,1],[0,1,1]]
        self.assertEqual(-1, maze_search(grid_2, flag))
        
        grid_3 = [[0,0,0],[0,1,1],[0,1,1]]
        self.assertEqual(-1, maze_search(grid_3, flag))

        grid_4 = [[1,1,1,1,1,1],[1,1,1,1,1,1],[1,1,1,1,1,1],[1,1,1,1,1,1]]
        self.assertEqual(8, maze_search(grid_4, flag))

        
if __name__ == "__main__":
    unittest.main()