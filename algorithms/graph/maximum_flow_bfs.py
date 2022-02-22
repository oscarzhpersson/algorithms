"""
Given a n*n adjacency array.
it will give you a maximum flow.
This version use BFS to search path.

Assume the first is the source and the last is the sink.

Time complexity - O(Ef)

example

graph = [[0, 16, 13, 0, 0, 0], 
        [0, 0, 10, 12, 0, 0], 
        [0, 4, 0, 0, 14, 0], 
        [0, 0, 9, 0, 0, 20], 
        [0, 0, 0, 7, 0, 4], 
        [0, 0, 0, 0, 0, 0]] 

answer should be

23

"""
import copy
import queue
import math

def maximum_flow_bfs(adjacency_matrix):
    #initial setting
    new_array = copy.deepcopy(adjacency_matrix)
    total = 0

    flagscond = {
        "Flag1": False,
        "Flag2": False,
        "Flag3": False,
        "Flag4": False,
        "Flag5": False,
        "Flag6": False,
        "Flag7": False,
        "Flag8": False,
        "Flag4-else": False,
        "Flag5-else": False,
        "Flag7-else": False
    }

    while(1):
        #Flag-2
        flagscond["Flag1"] = True

        #setting min to max_value
        min = math.inf
        #save visited nodes
        visited = [0]*len(new_array)
        #save parent nodes
        path = [0]*len(new_array)
        
        #initialize queue for BFS
        bfs = queue.Queue()

        #initial setting 
        visited[0] = 1
        bfs.put(0)

        #BFS to find path
        while(bfs.qsize() > 0):
            flagscond["Flag2"] = True

            #pop from queue
            src = bfs.get()
            for k in range(len(new_array)):
                flagscond["Flag3"] = True

                #checking capacity and visit
                if(new_array[src][k] > 0 and visited[k] == 0 ):
                    flagscond["Flag4"] = True

                    #if not, put into queue and chage to visit and save path
                    visited[k] = 1
                    bfs.put(k)
                    path[k] = src

                else:
                    flagscond["Flag4-else"] = True
            
        #if there is no path from src to sink
        if(visited[len(new_array) - 1] == 0):
            flagscond["Flag5"] = True
            break
        else:
            flagscond["Flag5-else"] = True
        
        #initial setting
        tmp = len(new_array) - 1

        #Get minimum flow
        while(tmp != 0):
            flagscond["Flag6"] = True

            #find minimum flow
            if(min > new_array[path[tmp]][tmp]):
                flagscond["Flag7"] = True
                min = new_array[path[tmp]][tmp]
            else:
                flagscond["Flag7-else"] = True

            tmp = path[tmp]

        #initial setting
        tmp = len(new_array) - 1

        #reduce capacity
        while(tmp != 0):
            flagscond["Flag8"] = True

            new_array[path[tmp]][tmp] = new_array[path[tmp]][tmp] - min
            tmp = path[tmp]

        total = total + min

    return total, flagscond
