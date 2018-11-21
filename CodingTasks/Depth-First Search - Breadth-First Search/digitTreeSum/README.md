# Problem
We're going to store numbers in a tree. Each node in this tree will store a single digit (from 0 to 9), and each path from root to leaf encodes a non-negative integer.

Given a binary tree t, find the sum of all the numbers encoded in it.

Example

For  

    t = {  
    "value": 1,  
    
    "left": {  
    
        "value": 0,  
        
        "left": {  
            "value": 3,  
            "left": null,  
            "right": null  
        },  
        "right": {  
            "value": 1,  
            "left": null,  
            "right": null  
        }  
    },  
    "right": {  
        "value": 4,  
        "left": null,   
        "right": null  
    }  
    }  
    
the output should be  
digitTreeSum(t) = 218.  
There are 3 numbers encoded in this tree:  

Path 1->0->3 encodes 103  
Path 1->0->1 encodes 101  
Path 1->4 encodes 14  
and their sum is 103 + 101 + 14 = 218.  

    t = {  
        "value": 0,  
        "left": {  
            "value": 9,  
            "left": null,  
            "right": null  
        },  
        "right": {  
            "value": 9,   
            "left": {  
                "value": 1,  
                "left": null,  
                "right": null  
            },  
            "right": {    
                "value": 3,  
                "left": null,  
                "right": null  
            }  
        }  
    }  
    
the output should be  
digitTreeSum(t) = 193.  
Because 09 + 091 + 093 = 193  

# Solution
```python
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
```
