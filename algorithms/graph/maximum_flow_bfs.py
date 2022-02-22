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

    while(1):
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
            #pop from queue
            src = bfs.get()
            for k in range(len(new_array)):
                #checking capacity and visit
                if(new_array[src][k] > 0 and visited[k] == 0 ):
                    #if not, put into queue and chage to visit and save path
                    visited[k] = 1
                    bfs.put(k)
                    path[k] = src
                    
        #print("Path", path)
        #if there is no path from src to sink
        if(visited[len(new_array) - 1] == 0):
            break
        
        #initial setting
        tmp = len(new_array) - 1

        #Get minimum flow
        while(tmp != 0):
            #find minimum flow
            if(min > new_array[path[tmp]][tmp]):
                min = new_array[path[tmp]][tmp]
            tmp = path[tmp]

        #initial setting
        tmp = len(new_array) - 1

        #reduce capacity
        while(tmp != 0):
            new_array[path[tmp]][tmp] = new_array[path[tmp]][tmp] - min
            tmp = path[tmp]

        total = total + min
    
    return total

'''
By doing some tests for this algorithm the conclusion is that this specific algorihm cannot be refactored without large structural change to the entire function
The reason that this cannot be restructured is just by the way the entire function is set up. At line 33 there is a while loop that runs until there is no path not
covered and then it breaks from that loop, it ties together and makes the BFS search and maximum flow tied together. By doing so there is no simple way for the function to be refactored into smaller functions which would help the CC of this
funciton. 
'''


def main():
    graph = [[0, 16, 13, 0, 0, 0],
            [0, 0, 10, 12, 0, 0],
            [0, 4, 0, 0, 14, 0],
            [0, 0, 9, 0, 0, 20],
            [0, 0, 0, 7, 0, 4],
            [0, 0, 0, 0, 0, 0]]

    #print(maximum_flow_bfs(graph))

    graph = [[0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0]]

    print(maximum_flow_bfs(graph))
   
'''
    graph = [[0, 16, 13, 0, 0, 0],
             [0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0]]

    total, flags = maximum_flow_bfs(graph)
    print(flags)
    print(total)

    graph = [[0, 1, 1, 1, 1, 1],
             [1, 0, 0, 0, 0, 0],
             [1, 0, 0, 0, 0, 0],
             [1, 0, 0, 0, 0, 0],
             [1, 0, 0, 0, 0, 0],
             [1, 0, 0, 0, 0, 0]]

    total, flags = maximum_flow_bfs(graph)
    print(flags)
    print(total)

'''
'''
    graph = [[1000, 1000, 1000, 1000, 1000, 1000],
             [1000, 1000, 1000, 1000, 1000, 1000],
             [1000, 1000, 1000, 1000, 1000, 1000],
             [1000, 1000, 1000, 1000, 1000, 1000],
             [1000, 1000, 1000, 1000, 1000, 1000],
             [1000, 1000, 1000, 1000, 1000, 1000]]

    total, flags = maximum_flow_bfs(graph)
    print(flags)
    print(total)
    print("Len of flags: ", len(flags))
'''


'''
    graph2 = []
    total, flags2 = maximum_flow_bfs(graph2)
    print(flags2)
    print(total2)
    print("Len of flags: ", len(flags))
    
'''
'''
    graph3 = [[0, 16, 13, 0, 0, 0],
            [0, 0, 10, 12, 0, 0],
            [0, 4, 0, 0, 14, 0],
            [0, 0, 9, 0, 0, 20]]
    total3, flags3 = maximum_flow_bfs(graph3)
    print(flags3)
    print(total3)
    print("Len of flags: ", len(flags))
'''
'''
    graph4 = [[0, 16, 13, 0, 0, 0]]
    total4, flags4 = maximum_flow_bfs(graph4)
    print(flags4)
    print(total4)
    print("Len of flags: ", len(flags))
'''

if __name__ == "__main__":
    main()
