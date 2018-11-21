# Problem
The sum of a subtree is the sum of all the node values in that subtree, including its root.

Given a binary tree of integers, find the most frequent sum (or sums) of its subtrees.

# Solution
```python
# Definition for binary tree:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def mostFrequentSum(t):
        
    def findSums(t, nodesums): # find the sum of subtree at each node
        if t is None:
            return 0
        
        nodesums[t.value] = findSums(t.left, nodesums) + findSums(t.right, nodesums) + nodesums.get(t.value, 0) + t.value
        
        return nodesums[t.value]
        
    nodesums = {}
    findSums(t, nodesums)
    
    countsums = {} # count frequency of each sum
    for eachsum in nodesums: 
        subtreeSum = nodesums[eachsum]
        countsums[subtreeSum] = countsums.get(subtreeSum, 0) + 1


    frequent_sums = set()
    frequency = 0
    
    for sums in countsums:
        if countsums[sums] > frequency:
            frequency = countsums[sums]
            frequent_sums.clear()
            frequent_sums.add(sums)
        if countsums[sums] == frequency:
            frequent_sums.add(sums)
    
    return sorted(list(frequent_sums))
```
