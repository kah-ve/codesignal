def feedingTime(classes):
    
    N = len(classes)
    colorArr = [0] * N
    
    #creating the graph out of the classes
    graph = [[0 for _ in range(N)] for _ in range(N)] # 2D array for graph
    classes = [set(c) for c in classes]
    
    # iterate through set and check where there are intersections
    for i in range(N-1):
        for j in range(i+1, N):
            if classes[i].intersection(classes[j]):
                graph[i][j] = 1
                graph[j][i] = 1
    
    def isColorable(curr, colorArr, color):
        for nei in range(N):
            if graph[curr][nei] == 1 and colorArr[nei] == color:
                return False # a neighbor shares the color, not colorable with this color
        return True
    
    def coloringGraph(curr, k):
        if curr == N:
            return True # it has recursed till past the last node and has passed the colorability check
        
        for color in range(1, k+1): # see if k coloring works by trial and error of different colors
            if isColorable(curr, colorArr, color):
                colorArr[curr] = color # colored the current node
                
                # now check neighbors recursively
                if coloringGraph(curr+1, k):
                    return True # get here if we iterate through all neighbors and curr = N at the top, then it passed coloring test
                
                # if above test fails, then we know that the neighbors are not k colorable, reset to try again in future
                colorArr[curr] = 0
    
        return False # we haven't returned True until this point so the coloring range does not work with k, return False
                
        
    for k in range (1, 6):
        if coloringGraph(0, k):
            return k # found a k coloring that works
    
    return -1 # no coloring found within 5 colorable, so return -1
