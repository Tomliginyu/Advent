import numpy as np
import matplotlib.pyplot as plt

TALL = 71
WIDE = 71
START = (0,0)
END = (0,0)

def valid_node(node, size_of_grid):
    """Checks if node is within the grid boundaries."""
    if node[0] < 0 or node[0] >= size_of_grid:
        return False
    if node[1] < 0 or node[1] >= size_of_grid:
        return False
    return True

def isValidForCheat(node,size_of_grid,curren_node):
    global mapS
    if node[0] == 0 or node[0] == size_of_grid - 1:
        return False
    if node[1] == 0 or node[1] == size_of_grid - 1:
        return False
    if mapS[node] != '#':
        return False
    return True
    
def up(node):
    return (node[0]-1,node[1])

def down(node):
    return (node[0]+1,node[1])

def left(node):
    return (node[0],node[1]-1)

def right(node):
    return (node[0],node[1]+1)
    
def diff(node1,node2):
    tmp = node1
    
UP = (-1,0)
DOWN = (1,0)
RIGHT = (0,1)
LEFT = (0,-1)    

def printPath(rpt,icons,debug):
    global mapS
    if debug:
        for i in range(0,TALL):
            for j in range(0,WIDE):
                # if (i,j) == rpt[0]:
                    # print('1',end="")
                    # continue
                # if (i,j) == rpt[1]:
                    # print('2',end="")
                    # continue
                if (i,j) in rpt:
                    print('O',end="")
                    continue
                print(mapS[(i,j)],end="")
            print()
        print()

def printArray(rpt,icons,debug):
    global mapS
    if debug:
        for i in range(0,len(rpt)):
            for j in range(0,len(rpt[0])):
                print(rpt[i][j],end=" ")
            print()
        print()  
        
def backtrack(initial_node, desired_node, distances):
    global distListTo
    # idea start at the last node then choose the least number of steps to go back
    # last node
    path = [desired_node]

    size_of_grid = distances.shape[0]
    
    lastNode = (0,0)
    dist = 0
    distListTo[END] = dist
    
    # lastDirection = RIGHT
    while True:
        # check up down left right - choose the direction that has the least distance
        potential_distances = []
        potential_nodes = []
        potential_directions = []
        tdistances = distances.copy()

        directions = [up,down,left,right]
        tNode = (0,0)
        for direction in directions:
            node = direction(path[-1])
            tNode = direction((0,0))
            # print(lastNode,node,tdistances[node[0],node[1]])
            if valid_node(node, size_of_grid):
                potential_nodes.append(node)
                potential_distances.append(tdistances[node[0],node[1]])
        # printPath(path,{},True)
        # input()
        least_distance_index = np.argmin(potential_distances)
        path.append(potential_nodes[least_distance_index])
        lastNode = potential_nodes[least_distance_index]
        dist += 1
        distListTo[(lastNode)] = dist
        

        if path[-1][0] == initial_node[0] and path[-1][1] == initial_node[1]:
            break

    return list(reversed(path))

def dijkstra(initial_node, desired_node, obstacles):
    global distListFrom
    """Dijkstras algorithm for finding the shortest path between two nodes in a graph.

    Args:
        initial_node (list): [row,col] coordinates of the initial node
        desired_node (list): [row,col] coordinates of the desired node
        obstacles (array 2d): 2d numpy array that contains any obstacles as 1s and free space as 0s

    Returns:
        list[list]: list of list of nodes that form the shortest path
    """
    # initialize cost heuristic map
    obstacles = obstacles.copy()
    # obstacles should have very high cost, so we avoid them.
    obstacles *= 10000000
    # normal tiles should have 1 cost (1 so we can backtrack)
    obstacles += np.ones(obstacles.shape)
    # source and destination are free
    obstacles[initial_node[0],initial_node[1]] = 0
    obstacles[desired_node[0],desired_node[1]] = 0


    # initialize maps for distances and visited nodes
    size_of_floor = obstacles.shape[0]

    # we only want to visit nodes once
    visited = np.zeros([size_of_floor,size_of_floor],bool)

    # initiate matrix to keep track of distance to source node
    # initial distance to nodes is infinity so we always get a lower actual distance
    distances = np.ones([size_of_floor,size_of_floor]) * np.inf
    # initial node has a distance of 0 to itself
    distances[initial_node[0],initial_node[1]] = 0

    # start algorithm
    current_node = [initial_node[0], initial_node[1]]
    while True:
        directions = [up, down, left, right]
        for direction in directions:
            potential_node = direction(current_node)
            tNode = direction((0,0))
            if valid_node(potential_node, size_of_floor): # boundary checking
                if not visited[potential_node[0],potential_node[1]]: # check if we have visited this node before
                    #Need to do Direction Modification
                    # update distance to node
                    distance = distances[current_node[0], current_node[1]] + obstacles[potential_node[0],potential_node[1]]
                    
                    # update distance if it is the shortest discovered
                    if distance < distances[potential_node[0],potential_node[1]]:
                        distances[potential_node[0],potential_node[1]] = distance
                        

        # printPath([(current_node[0],current_node[1])],{},True)
        # mark current node as visited
        visited[current_node[0]  ,current_node[1]] = True

        # select next node
        # by choosing the the shortest path so far
        t=distances.copy()
        # we don't want to visit nodes that have already been visited
        t[np.where(visited)]=np.inf
        # choose the shortest path
        node_index = np.argmin(t)

        # convert index to row,col.
        node_row = node_index//size_of_floor
        node_col = node_index%size_of_floor

        # update current node.
        current_node = (node_row, node_col) #, lastDirection)

        # stop if we have reached the desired node
        if current_node[0] == desired_node[0] and current_node[1]==desired_node[1]:
            break

    # backtrack to construct path
    return backtrack(initial_node,desired_node,distances)
    
def dijkstraMoD(initial_node, desired_node, obstacles):
    global cheats, orig, mapS,obsRemoved,obsStart,distListFrom
    """Dijkstras algorithm for finding the shortest path between two nodes in a graph.

    Args:
        initial_node (list): [row,col] coordinates of the initial node
        desired_node (list): [row,col] coordinates of the desired node
        obstacles (array 2d): 2d numpy array that contains any obstacles as 1s and free space as 0s

    Returns:
        list[list]: list of list of nodes that form the shortest path
    """
    # initialize cost heuristic map
    obstacles = obstacles.copy()
    # obstacles should have very high cost, so we avoid them.
    obstacles *= 10000000
    # normal tiles should have 1 cost (1 so we can backtrack)
    obstacles += np.ones(obstacles.shape)
    # source and destination are free
    obstacles[initial_node[0],initial_node[1]] = 0
    obstacles[desired_node[0],desired_node[1]] = 0


    # initialize maps for distances and visited nodes
    size_of_floor = obstacles.shape[0]

    # we only want to visit nodes once
    visited = np.zeros([size_of_floor,size_of_floor],bool)

    # initiate matrix to keep track of distance to source node
    # initial distance to nodes is infinity so we always get a lower actual distance
    distances = np.ones([size_of_floor,size_of_floor]) * np.inf
    # initial node has a distance of 0 to itself
    distances[initial_node[0],initial_node[1]] = 0

    # start algorithm
    current_node = [initial_node[0], initial_node[1]]
    distListFrom[(initial_node[0],initial_node[1])] = 0
    while True:
        directions = [up, down, left, right]
        for direction in directions:
            potential_node = direction(current_node)
            tmp1 = direction(potential_node)
            if isValidForCheat(potential_node, size_of_floor,current_node) and potential_node not in obsRemoved:
                # obsCPY = obstacles.copy()
                # obsCPY[potential_node] = 0
                # nPath = dijkstra((current_node[0],current_node[1]),END,obsCPY)
                # newP = orig - (len(nPath)-1)
                # print(newP)
                # printPath([(current_node[0],current_node[1]),(potential_node)],{},True)   
                # if str(newP) in cheats.keys():
                    # cheats[str(newP)] += 1
                # else:
                    # cheats[str(newP)] = 1
                obsRemoved.add((potential_node))
                obsStart[(potential_node)] = [(current_node[0],current_node[1]),(tmp1[0],tmp1[1])]
            if valid_node(potential_node, size_of_floor): # boundary checking
                if not visited[potential_node[0],potential_node[1]]: # check if we have visited this node before
                    #Need to do Direction Modification
                    # update distance to node
                    distance = distances[current_node[0], current_node[1]] + obstacles[potential_node[0],potential_node[1]]
                    
                    # update distance if it is the shortest discovered
                    if distance < distances[potential_node[0],potential_node[1]]:
                        distances[potential_node[0],potential_node[1]] = distance
                        distListFrom[(potential_node[0],potential_node[1])] = distance

        # printPath([(current_node[0],current_node[1])],{},True)
        # mark current node as visited
        visited[current_node[0]  ,current_node[1]] = True

        # select next node
        # by choosing the the shortest path so far
        t=distances.copy()
        # we don't want to visit nodes that have already been visited
        t[np.where(visited)]=np.inf
        # choose the shortest path
        node_index = np.argmin(t)

        # convert index to row,col.
        node_row = node_index//size_of_floor
        node_col = node_index%size_of_floor

        # update current node.
        current_node = (node_row, node_col) #, lastDirection)

        # stop if we have reached the desired node
        if current_node[0] == desired_node[0] and current_node[1]==desired_node[1]:
            break

    # backtrack to construct path
    return
    
    
if __name__ == "__main__":
    corr = set()
    global mapS, orig, cheats,obsRemoved,obsStart,distListTo,distListFrom
    #Read File
    map = []
    mapS = {}
    cheats = {}
    obsRemoved = set()
    obsStart = {}
    distListTo = {}
    distListFrom = {}
    with open("data1.txt", "r") as file:
        for line in file:
            map.append(line.replace('\n',""))
            
    TALL = len(map)
    WIDE = len(map[0])
    obs = []
    
    for i in range(0,TALL):
        for j in range(0,WIDE):
            mapS[(i,j)] = map[i][j]
            if map[i][j] == '#':
                obs.append((i,j))
                continue
            if map[i][j] == 'S':
                START = (i,j)
                continue
            if map[i][j] == 'E':
                END = (i,j)
                continue
            
    obstacles = np.zeros(shape=(TALL,WIDE), dtype=float)
    for ob in obs:
        obstacles[ob[0],ob[1]] = 1
    
    path = dijkstra(START,END,obstacles)
    orig = len(path)-1
    size_of_grid = TALL
    # printPath(path,{},True)
    print("Original Score:",orig)
    
    
    #Now Let's Cheat
    dijkstraMoD(START,END,obstacles)
    # print(distListTo)
    # print(distListFrom)
    # n1 = distListFrom[START]
    # n2 = distListTo[END]
    # print(n1,n2)
    for ob in obsRemoved:
        nStart = obsStart[ob]
        if nStart[0] in distListFrom.keys() and nStart[1] in distListTo.keys():
            n1 = distListFrom[nStart[0]]
            n2 = distListTo[nStart[1]]
            newP = orig - int((n1+n2+1)-1) - 2
            if str(newP) in cheats.keys():
                cheats[str(newP)] += 1
            else:
                cheats[str(newP)] = 1
        
    ssKeys = list(cheats.keys())
    sKeys = [int(item) for item in ssKeys]
    sKeys.sort()
    sum = 0
    for s in sKeys:
        print(str(s),cheats[str(s)])
        if int(s) > 99:
            sum += cheats[str(s)]
    print("Cheats that save at least 100 seconds:",sum)
    
    
    