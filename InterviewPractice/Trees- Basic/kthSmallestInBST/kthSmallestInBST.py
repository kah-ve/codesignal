#
# Definition for binary tree:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def kthSmallestInBST(t, k):
    
    def traverse(t):
        if t:
            for i in traverse(t.left):
                yield i
            yield t.value
            for i in traverse(t.right):
                yield i
    
    for i in traverse(t):
        if k == 1:
            return i
        else:
            k -= 1
