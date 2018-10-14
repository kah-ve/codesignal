#
# Definition for binary tree:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def deleteFromBST(t, queries):
    
    # find the max value in the left tree branch
    def findMax(t):
        while t.right is not None:
            t = t.right
        return t.value
    
    # remove the max value from the left tree branch after we assign it
    def removeMax(t):
        if t.right is None:
            return t.left
        else:
            t.right = removeMax(t.right)
        return t
    
    # recursively check for query in the root value and iterate through the branches
    def deleteQuery(t, query):
         
        if t is None:
             return None
            
        if query < t.value:
            t.left = deleteQuery(t.left, query)
        elif  query > t.value:
            t.right = deleteQuery(t.right, query)
        else:
            #  query == t.value
            if t.left is None and t.right is None: # leaf
                return None
            elif t.left is None: # only right branch
                return t.right
            else:
                # both left and right branches exist
                maxOfLeft = findMax(t.left)
                t.value = maxOfLeft
                t.left = removeMax(t.left)
        return t

    for query in queries:
        t = deleteQuery(t, query)
    return t


