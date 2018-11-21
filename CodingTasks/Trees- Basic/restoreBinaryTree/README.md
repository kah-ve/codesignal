# Problem
Let's define inorder and preorder traversals of a binary tree as follows:

Inorder traversal first visits the left subtree, then the root, then its right subtree;
Preorder traversal first visits the root, then its left subtree, then its right subtree.
For example, if tree looks like this:

```
    1
   / \
  2   3
 /   / \
4   5   6
```

then the traversals will be as follows:

    Inorder traversal: [4, 2, 1, 5, 3, 6]
    Preorder traversal: [1, 2, 4, 3, 5, 6]

Given the inorder and preorder traversals of a binary tree t, but not t itself, restore t and return it.

# Solution
```python
# Definition for binary tree:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def restoreBinaryTree(inorder, preorder):
    
    #  create a recursive function that uses preorder[0] to separate into left and right branches, makes the root
    #  at preorder[0], creates this Tree with class Tree, and for right and left we recursively send those branches
    
    #base cases
    if len(preorder) == 0:
        return None
    if len(preorder) == 1:
        return Tree(preorder[0])
    
    root = Tree(preorder[0])
    divider = inorder.index(preorder[0])
    leftinorder = inorder[0:divider]
    rightinorder = inorder[divider+1:]
    #  note for preorder that you can simply take the number of elements in left inorder, ie preorder[1:len(inorderleft)] 
    #  since all the elements on the left branch will be before right branch in preorder
    leftpreorder = preorder[1:divider+1]
    rightpreorder = preorder[divider+1:]
    root.left = restoreBinaryTree(leftinorder, leftpreorder)
    root.right = restoreBinaryTree(rightinorder, rightpreorder)
    
    return root
```
