# Problem
You are the head zookeeper at a large zoo. You've been contacted by schools in the area that want to bring in classes so that students can feed the animals. The animals can only be fed once a day, so no two classes can come on the same day if they want to feed the same animals.

You have a list classes, such that classes[i] is a list of animals that the ith class wants to feed. Classes i and j cannot come on the same day if an animal in classes[i] also appears in classes[j] (for i ≠ j). Your job is to determine the minimum number of days you would need to have all the classes come to feed the animals if they can all come within 5 days. If it isn't possible for all the classes to come within 5 days, return -1 instead.

# Solution
```python
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
```
