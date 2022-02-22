from collections import deque

'''
BFS time complexity : O(|E| + |V|)
BFS space complexity : O(|E| + |V|)

do BFS from (0,0) of the grid and get the minimum number of steps needed to get to the lower right column

only step on the columns whose value is 1

if there is no path, it returns -1

Ex 1)
If grid is
[[1,0,1,1,1,1],
 [1,0,1,0,1,0],
 [1,0,1,0,1,1],
 [1,1,1,0,1,1]], 
the answer is: 14

Ex 2)
If grid is
[[1,0,0],
 [0,1,1],
 [0,1,1]], 
the answer is: -1
'''

def maze_search(maze, flag):
    BLOCKED, ALLOWED = 0, 1
    UNVISITED, VISITED = 0, 1

    initial_x, initial_y = 0, 0

    if maze[initial_x][initial_y] == BLOCKED:
        flag[0] += 1
        return -1
    
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

    height, width = len(maze), len(maze[0])

    target_x, target_y = height - 1, width - 1

    queue = deque([(initial_x, initial_y, 0)])

    is_visited = maze_search_is_visited_array(UNVISITED, width, height)
    is_visited[initial_x][initial_y] = VISITED

    while queue:
        x, y, steps = queue.popleft()

        confirm_target(x, y, target_x, target_y, flag)

        for dx, dy in directions:
            new_x = x + dx
            new_y = y + dy

            if not (0 <= new_x < height and 0 <= new_y < width):
                flag[4] +=1
                continue

            if maze[new_x][new_y] == ALLOWED and is_visited[new_x][new_y] == UNVISITED:
                queue.append((new_x, new_y, steps + 1))
                flag[5] += 1
                is_visited[new_x][new_y] = VISITED
            flag[2] += 1
        flag[1] += 1


    return -1 

def maze_search_is_visited_array(UNVISITED, width, height):
    return [[UNVISITED for w in range(width)] for h in range(height)]

def confirm_target(x, y, target_x, target_y, flag):
    if x == target_x and y == target_y:
        flag[3] += 1
        return steps
    return