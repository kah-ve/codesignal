#
# Definition for binary tree:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def traverseTree(t):
    
    # add the root to the queue
    # for each node, add its children to the queue from left to right
    result = []
    
    queue = []
    queue.insert(0, t)
    
    while queue:
        elmnt = queue.pop()
        
        if elmnt:
            result.append(elmnt.value)
        else:
            continue
        
        if elmnt.left:
            queue.insert(0, elmnt.left)
        if elmnt.right:
            queue.insert(0, elmnt.right)
    
    return result
            
        
        
