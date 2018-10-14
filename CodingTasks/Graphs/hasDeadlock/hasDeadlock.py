def hasDeadlock(connections):   
    # use fact that a cyclic graph must be bipartite
    
    color = [0] * len(connections) # all nodes with color 0 are not visited
    
    def DFS(node):
        if color[node] == 0:
            color[node] = 1 # once node is visited color is made 1
            for nei in connections[node]: 
                if color[nei] == 1: # if node with color 1 has a neighbor with color 1, then cycle
                    return True
                if DFS(nei): # recursively run through the neighbors with DFS and see if exists cycle
                    return True
            color[node] = 2 # base case of a sink node will start with color = 2 then it will 
                            # recursively run backwards and keep changing all to 2s if no cycle
                            # is found in the neigboring nodes that are not colored 2
    
    for i in range(len(connections)):
        check = DFS(i)
        if check:
            return True
    return False

