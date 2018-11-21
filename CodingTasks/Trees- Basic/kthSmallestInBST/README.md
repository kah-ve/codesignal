# Problem
A tree is considered a binary search tree (BST) if for each of its nodes the following is true:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and the right subtrees must also be binary search trees.
Given a binary search tree t, find the kth smallest element in it.

Note that kth smallest element means kth element in increasing order. See examples for better understanding.

Example

For  


                3
           /         \
          1           5
                     /  \
                    4    6

the output should be
`kthSmallestInBST(t, k) = 5.`
# Solution
```python
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
```
