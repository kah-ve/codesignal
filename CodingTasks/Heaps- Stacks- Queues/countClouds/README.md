# Problem
Given a 2D grid skyMap composed of '1's (clouds) and '0's (clear sky), count the number of clouds. A cloud is surrounded by clear sky, and is formed by connecting adjacent clouds horizontally or vertically. You can assume that all four edges of the skyMap are surrounded by clear sky.
# Solution
```python
def countClouds(skyMap):
    
    # checks if the coords are in the bounds of the skyMap
    def inBounds(x, y):
        if 0 <= x < len(skyMap) and 0 <= y < len(skyMap[0]):
            return True
        return False
    
    # checks the neighbors of the input coord and yields the coords that have a 1
    def checkNeighbors(x, y):
        for near_x, near_y in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
            if inBounds(near_x, near_y) and skyMap[near_x][near_y] == '1':
                yield near_x, near_y
                
    visited_coords = set()
    num_clouds = 0
    
    # iterate over the skyMap and send each coord to checkNeighbors. If coord has a '1'
    # then add it to the seen_coords after also iterating through all of its neighbors
    # that also have a '1' by using a stack.
    for row in range(len(skyMap)):
        for col in range(len(skyMap[0])):
            curr = skyMap[row][col]
            if curr == '1' and (row, col) not in visited_coords:
                stack = [(row, col)]
                visited = {(row, col)}
                num_clouds += 1
                # Follow all neighbors that have a '1' and add to visited set
                while (stack):
                    toCheck = stack.pop()
                    for x, y in checkNeighbors(*toCheck):
                        if (x, y) not in visited:
                            stack.append((x, y))
                            visited.add((x,y))
                visited_coords |= visited
    
    return num_clouds
```
