# Problem
Given a binary tree of integers t, return its node values in the following format:

The first element should be the value of the tree root;
The next elements should be the values of the nodes at height 1 (i.e. the root children), ordered from the leftmost to the rightmost one;
The elements after that should be the values of the nodes at height 2 (i.e. the children of the nodes at height 1) ordered in the same way;
Etc.

Example

For

    t = {
        "value": 1,
        "left": {
            "value": 2,
            "left": null,
            "right": {
                "value": 3,
                "left": null,
                "right": null
            }
        },
        "right": {
            "value": 4,
            "left": {
                "value": 5,
                "left": null,
                "right": null
            },
            "right": null
        }
    }
the output should be
`traverseTree(t) = [1, 2, 4, 3, 5].`

This tree looks like this:

       1
     /   \
    2     4
     \   /
      3 5
# Solution
```python
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
```
