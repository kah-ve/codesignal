#
# Definition for binary tree:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def isSubtree(t1, t2):
    
    def checkSubtree(t1, t2):
        if t1 is None and t2 is None:
            return True        
        if t1 is None or t2 is None:
            return False
    
        return (t1.value == t2.value and checkSubtree(t1.left, t2.left) and checkSubtree(t1.right, t2.right))

    def iterateTree(t1, t2):
        if t2 is None:
            return True
        
        if t1 is None:
            return False
        
        if checkSubtree(t1, t2):
            return True
        
        return (iterateTree(t1.left, t2) or iterateTree(t1.right, t2))
    
    return iterateTree(t1, t2)
            
        
    
