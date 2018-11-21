Note: Try to solve this task in O(n2) time, where n is a number of vertices, since this is what you'll be asked to do during an interview.

Sue is a network administrator who consults for companies that have massive Local Area Networks (LANs). The computers are connected together with network cables, and Sue has been brought in to evaluate the company’s network. The networks are huge, and she wants to ensure that no single network cable failure can disconnect the network. Any cable that fails that leaves the network in two or more disconnected pieces is called a single point of failure.

She labels the different network devices from 0 to n - 1. She keeps an n × n matrix connections, where connections[i][j] = 1 if there is a network cable directly connecting devices i and j, and 0 otherwise. Write a function that takes the matrix of connections, and returns the number of cables that are a single point of failure.

    def singlePointOfFailure(connections):    
        N = len(connections)
        time = 0 # will be used to assign ids to nodes
        lowlink = [float("Inf")] * N # holds the id number of lowest id node can reach
        ids = [float("Inf")] * N # holds each nodes id number
        visited = [False] * N 
        bridges = 0

        def dfs(curr, parent = None):
            nonlocal time, bridges
            if not visited[curr]:
                visited[curr] = True
                lowlink[curr] = time # lowest link is its own id at first
                ids[curr] = time # give the node its id
                time += 1

                #now check neighbors of current node
                for nei, check in enumerate(connections[curr]):
                    if nei == parent or not check: # if nei is parent then ignore it or if connection is 0
                        continue
                    if not visited[nei]:
                        dfs(nei, curr)
                        lowlink[curr] = min(lowlink[nei], lowlink[curr]) # after the recursive dfs call, check to see if neighbors lowlink is lower
                        if lowlink[nei] > ids[curr]: # if the lowlink at a neighbor node is greater than the id of the current node, its a bridge
                            bridges += 1
                    else:
                        lowlink[curr] = min(lowlink[curr], ids[nei]) # if neighbor already visited, check to see if neighbors id is lower

        for i in range(N):
            dfs(i)

        return bridges

