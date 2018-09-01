You have a connected directed graph that has positive weights in the adjacency matrix g. The graph is represented as a square matrix, where g[i][j] is the weight of the edge (i, j), or -1 if there is no such edge.

Given g and the index of a start vertex s, find the minimal distances between the start vertex s and each of the vertices of the graph.

Example

For
'''
g = [[-1, 3, 2],
     [2, -1, 0],
     [-1, 0, -1]]
'''

and s = 0, the output should be
graphDistances(g, s) = [0, 2, 2].

Example

The distance from the start vertex 0 to itself is 0.
The distance from the start vertex 0 to vertex 1 is 2 + 0 = 2.
The distance from the start vertex 0 to vertex 2 is 2.
