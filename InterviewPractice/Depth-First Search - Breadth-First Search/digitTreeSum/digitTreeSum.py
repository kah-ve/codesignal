#
# Definition for binary tree:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None


def digitTreeSum(t):

    sumset = set()
    
    # dfs
    def dfs(node, currsum):
        
        if not node:
            return 0
        
        newsum = currsum*10 + node.value
        
        # end of path, return sum
        if not node.left and not node.right:
            return newsum
        
        # recurse through left and right branches, returning the sum only when end of path
        return dfs(node.left, newsum) + dfs(node.right, newsum)
        
    
    return dfs(t, 0)
    
