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

        


