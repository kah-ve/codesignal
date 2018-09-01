#
# Definition for binary tree:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def largestValuesInTreeRows(t):

    if not t:
        return []
    
    # value at key is the largest at depth key in tree
    largest = {}
    queue = []
    queue.insert(0, (t, 0))
    
    # BFS
    while queue:
        curr, depth = queue.pop()
                
        if largest.get(depth, 0):
            if curr.value > largest[depth]:
                largest[depth] = curr.value
        else:
            largest[depth] = curr.value
            
        if curr.left:
            queue.insert(0, (curr.left, depth+1))
        if curr.right:
            queue.insert(0, (curr.right, depth+1))
        
    result = []
    for i in sorted(largest.keys()):
        result.append(largest[i])
    
    return result
        
        
        
        
    
