def longestPath(fileSystem):
    
    maxlen = 0
    pathDict = {0: 0}
    
    for file in fileSystem.split("\f"):
        depth = file.count('\t')
        name = len(file) - depth
        if '.' in file:
            # end of path
            maxlen = max(maxlen, pathDict[depth] + name)
        else:
            # not at end of path, save into dictionary and account for forward slash
            pathDict[depth+1] = pathDict[depth] + name + 1
    return maxlen
    
