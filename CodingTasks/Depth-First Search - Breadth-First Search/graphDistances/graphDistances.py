def graphDistances(g, s):
    N = len(g)
    for x in range(N):
        for y in range(N):
            if g[x][y] == -1:
                g[x][y] = float('inf')
                
    for k in range(N):
        for i in range(N):
            for j in range(N):
                g[i][j] = min(g[i][j], g[i][k] + g[k][j])
    
    g[s][s] = 0 # distance to self is 0
    return g[s][:]
