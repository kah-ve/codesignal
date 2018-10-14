#
# Definition for binary tree:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def isTreeSymmetric(t):

    def checkIfMirror(left, right):
        if left == None and right == None:
            return True
        
        if (left != None and right != None):
            if left.value == right.value:
                return checkIfMirror(left.left, right.right) and checkIfMirror(left.right, right.left)
        
        return False
    
    return checkIfMirror(t, t)
