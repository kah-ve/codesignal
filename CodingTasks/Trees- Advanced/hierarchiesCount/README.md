# Problem
Since you became a director of a large company, you came to know all of your n employees perfectly well. You carefully studied their relationships and came up with a list of pairs of workers who respect one another. You are sure that in a healthy environment subordinates should respect their immediate superiors, which is why you would like to change the hierarchy in the company according to the list you composed. This hierarchy should be represented by a rooted tree, and for each pair of employees a, b, a is an immediate superior of b (or the other way round) if and only if a respects b and vice versa.

Given the number of people in you company n and the respectList you created, calculate the number of different hierarchies you can create.

Example

For `n = 4` and `respectList = [[0, 1], [1, 2], [2, 3], [3, 0], [1, 3]]`,
the output should be
`hierarchiesCount(n, respectList) = 32`.

Here are all possible hierarchies:

    (0 -- 1), (1 -- 2), (2 -- 3);  
    (1 -- 2), (2 -- 3), (3 -- 0);  
    (2 -- 3), (3 -- 0), (0 -- 1);  
    (3 -- 0), (0 -- 1), (1 -- 2);  
    (1 -- 0), (1 -- 2), (1 -- 3);  
    (3 -- 0), (3 -- 1), (3 -- 2);  
    (1 -- 2), (1 -- 3), (3 -- 0);  
    (1 -- 0), (1 -- 3), (3 -- 2).  

Each of them can be rooted at any of 4 employees, so the answer equals the number of hierarchies in the list above multiplied by 4.

# Solution
```python
# finding the determinant
def det(m):
    n = len(m)
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(i+1, n-1):
                m[j][k] = m[j][k] * m[i][i] - m[j][i] * m[i][k]
                if i > 0:
                    m[j][k] = m[j][k] // m[i-1][i-1]
    return m[-2][-2]


def hierarchiesCount(n, respectList):
    
    mod = 10**9 + 7
    if n == 1:
        return 1
    
    # use kirchhoff's theorem, create the laplacian = degree matrix - adjacency matrix
    # or degree on diagonals and -1 at adjacencies
    
    # create a 2D zero array
    laplacian = [ [0] * n for _ in range(n)]
    
    # degree of node at diagonals and -1 at adjacencies
    for i, j in respectList:
        laplacian[i][i] += 1
        laplacian[j][j] += 1
        laplacian[i][j] = -1
        laplacian[j][i] = -1
        
    # take det for number of spanning trees
    result = (det(laplacian) % mod) * n
    
    return result % mod
```
