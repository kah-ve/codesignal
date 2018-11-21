# Problem
A tree is considered a binary search tree (BST) if for each of its nodes the following is true:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and the right subtrees must also be binary search trees.
Removing a value x from a BST t is done in the following way:

If there is no x in t, nothing happens;
Otherwise, let t' be a subtree of t such that t'.value = x.
If t' has a left subtree, remove the rightmost node from it and put it at the root of t';
Otherwise, remove the root of t' and its right subtree becomes the new t's root.
For example, removing 4 from the following tree has no effect because there is no such value in the tree:
```
    5
   / \
  2   6
 / \   \
1   3   8
       /
      7
```
Removing 5 causes 3 (the rightmost node in left subtree) to move to the root:
```
    3
   / \
  2   6
 /     \
1       8
       /
      7
```
And removing 6 after that creates the following tree:
```
    3
   / \
  2   8
 /   /
1   7
```
You're given a binary search tree t and an array of numbers queries. Your task is to remove queries[0], queries[1], etc., from t, step by step, following the algorithm above. Return the resulting BST.

# Solution
```python
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
```
