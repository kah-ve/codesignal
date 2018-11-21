# Problem
As a director of a large company, you try to do your best to make the working environment as efficient as possible. However, it's difficult to do so when even the hardware used in the office is not efficient: there are too many wires connecting your employees' computers.

Naturally, you decided to minimize their number by getting rid of some wires. There's only one constraint: if it is possible to deliver information from one computer to another one using the wires, it should still be possible to do so after the renovation. You would also like to minimize the total wires length, because the longer the wires, the more it possible for you to trip over them at some point.

Given the plan of your n office computers and the wires connecting them, find the minimum resulting length of the wires after removing some of them according to the constraints above

Example

For n = 7 and

        wires = [[0, 1, 1], [2, 0, 2], [1, 2, 3], [3, 4, 1],  
                 [4, 5, 2], [5, 6, 3], [6, 3, 2]]
         
the output should be networkWires(n, wires) = 8.



The best way is to remove wires 3 and 6 (1-based).

# Solution
```python
## Solution Using Graphs
# transform into a graph 
def createGraph(graph, wires):
    for eachedge in wires:
        graph[eachedge[0]] = (graph.get(eachedge[0], []) + 
                                           [(eachedge[1], eachedge[2])])
        graph[eachedge[1]] = (graph.get(eachedge[1], []) + 
                                           [(eachedge[0], eachedge[2])])


# helper function to find visitable nodes from a node
def findVisitableNodes(g, node, visitable, visitable_array):
    if node in g:
        for nei, weight in g[node]:
            if nei not in visitable:
                visitable.add(nei)
                findVisitableNodes(g, nei, visitable, visitable_array)
    else:
        pass
      
# find all connected components
def findConnectedComponents(g, visitable_array, n):
    for node in range(n):
        breakOut = False
        for eachComponent in visitable_array:
            if node in eachComponent:
                breakOut = True
                break # node isn't a new connected component, go to next node
        if breakOut:
            continue
        # node is not part of the connected components we've seen so far
        seen = set()
        findVisitableNodes(g, node, seen, visitable_array)
        if len(seen) != 0:
            visitable_array.append(seen)


# check to see if the components of the graph after removing edges and original components are the same
def areSame(check_array, visitable_array):
    areSame = True
    if len(check_array) != len(visitable_array):
        areSame = False
        return areSame
    for eachSet in visitable_array:
        if eachSet not in check_array:
            areSame = False
            return areSame
    return areSame


# convert from edges to components that we see in those edges        
def edgesToComponents(edgesToKeep, visitable_array, n):
        new_wires = []
        graph = {}
        for i, j, k in edgesToKeep:
            edge = [i, j, k]
            new_wires.append(edge)


        createGraph(graph, new_wires)
        findConnectedComponents(graph, visitable_array, n)


def networkWires(n, wires):


    # if no edges, or no nodes return 0
    if not wires:
        return 0
    elif n == 0:
        return 0
      
    graph = {}
    min_weight = 0


    createGraph(graph, wires)
    visitable_array = []
    findConnectedComponents(graph, visitable_array, n)


    edgesToKeep = set()
    
    # add the minimum edge between two nodes if they go to the same component
    for node in range(n):
        if node in graph:
            if len(graph[node]) == 1: # one edge so need to keep
                tempEdge = (node, graph[node][0][0], graph[node][0][1])
                edgesToKeep.add(tempEdge)
                continue
            bestNode = [(0, 0, float('inf'))] * len(visitable_array)
            for nei1, weight1 in graph[node]:
                #need to change bestNode according to the component also, each edge might be to a different component. 
                for nei2, weight2 in graph[node]:
                    for indx, connComp in enumerate(visitable_array):
                        if nei1 in connComp and nei2 in connComp:
                            edgeOne = (node, nei1, weight1)
                            edgeTwo = (node, nei2, weight2)
                            if weight1 < weight2 and weight1 < bestNode[indx][2]:
                                bestNode[indx] = edgeOne
                            elif weight2 < weight1 and weight2 < bestNode[indx][2]:
                                bestNode[indx] = edgeTwo
                            elif weight1 == weight2 and weight1 < bestNode[indx][2]:
                                bestNode[indx] = edgeOne


            # after checking all neighbors, bestNode should be the one with lowest weight edge
            for indx, eachCompEdge in enumerate(bestNode):
                if eachCompEdge[2] != float('inf'):
                    x, y, z = eachCompEdge
                    newEdge = (y, x, z)
                    if newEdge not in edgesToKeep:
                        edgesToKeep.add(eachCompEdge)
                    
    # check to make sure the number and elements in components are the same after removing edges
    check_array = []
    edgesToComponents(edgesToKeep, check_array, n)
      
    while not(areSame(check_array, visitable_array)):
        # find smallest not-same component
        smallestindx = float('inf')
        smallestlen = float('inf')
        for indx, component in enumerate(check_array):
            if component not in visitable_array and len(component) < smallestlen:
                smallestlen = len(component)
                smallestindx = indx
        
        # find the minimum weighted edge to another component
        findFrom = check_array[smallestindx]
        minWeight = float('inf')
        minEdge = None
        
        for node in findFrom:
            connectedTo = graph[node]
            for nei, weight in connectedTo:
                edge = (node, nei, weight)
                if nei not in findFrom:
                    if weight < minWeight:
                        minWeight = weight
                        minEdge = edge
        
        # add this minEdge to edgesToKeep and loop to see if now components are the same
        edgesToKeep.add(minEdge)
        check_array = []
        edgesToComponents(edgesToKeep, check_array, n)
    
    alreadyAdded = set()
    for i, j, k in edgesToKeep:
        edge1 = (i, j, k)
        edge2 = (j, i, k)
        if edge1 not in alreadyAdded and edge2 not in alreadyAdded:
            min_weight += k
            alreadyAdded.add(edge1)
            alreadyAdded.add(edge2)
                              
    print("Output: ", min_weight)
    return min_weight
```
