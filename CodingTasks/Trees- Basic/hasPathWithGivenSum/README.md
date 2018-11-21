# Problem
Tree
```
      4
     / \
    1   3
   /   / \
  -2  1   2
    \    / \
     3  -2 -3
```
and `s = 7`, the output should be `hasPathWithGivenSum(t, s) = true.`

Given a binary tree t and an integer s, determine whether there is a root to leaf path in t such that the sum of vertex values equals s.

# Solution
```python
# Definition for binary tree:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def hasPathWithGivenSum(t, s):
    
    #  at each node subtract the value from s and use recursion.Ellipsis
    #  If a leaf has a value 0 then return True else False
    #  In the recursion make the final return an or statement with all True and Falses
    
    if(t == None and s!=0):
        return False
    elif (t == None and s == 0):
        return True
    
    s = s - t.value
    result = False
    
    if (s == 0 and t.left == None and t.right == None):
        return True
    else:
        if (t.left):
            result |= hasPathWithGivenSum(t.left, s)
        if (t.right):
            result |= hasPathWithGivenSum(t.right, s)
        return result
```
