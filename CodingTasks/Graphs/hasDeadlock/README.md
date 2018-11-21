# Problem
In a multithreaded environment, it's possible that different processes will need to use the same resource. A wait-for graph represents the different processes as nodes in a directed graph, where an edge from node i to node j means that the node j is using a resource that node i needs to use (and cannot use until node j releases it).

We are interested in whether or not this digraph has any cycles in it. If it does, it is possible for the system to get into a state where no process can complete.

We will represent the processes by integers 0, ...., n - 1. We represent the edges using a two-dimensional list connections. If j is in the list connections[i], then there is a directed edge from process i to process j.

Write a function that returns True if connections describes a graph with a directed cycle, or False otherwise.

# Solution
```python
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
```
