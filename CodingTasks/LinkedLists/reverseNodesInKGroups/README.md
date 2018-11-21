# Problem
Given a linked list l, reverse its nodes k at a time and return the modified list. k is a positive integer that is less than or equal to the length of l. If the number of nodes in the linked list is not a multiple of k, then the nodes that are left out at the end should remain as-is.

You may not alter the values in the nodes - only the nodes themselves can be changed.

Example

For `l = [1, 2, 3, 4, 5]` and `k = 2`, the output should be
`reverseNodesInKGroups(l, k) = [2, 1, 4, 3, 5];`

For `l = [1, 2, 3, 4, 5]` and `k = 1`, the output should be
`reverseNodesInKGroups(l, k) = [1, 2, 3, 4, 5];`

For `l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]` and `k = 3`, the output should be
`reverseNodesInKGroups(l, k) = [3, 2, 1, 6, 5, 4, 9, 8, 7, 10, 11].`

# Solution
```python
# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def reverseNodesInKGroups(l, k):
    mainlist = []
    curr = l
    track = 0
    
    while (curr):
        #  first check to see if we can run through for k values
        checkcurr = curr
        tempTrack = 0
        tempList = []
        while (checkcurr):
            tempTrack += 1
            checkcurr = checkcurr.next
            if (tempTrack == k):
                break
        #  if so then append those values reversed to the mainlist
        if tempTrack == k:
            for i in range(k):
                tempList.append(curr.value)
                curr = curr.next           
            tempList.reverse()
            mainlist.extend(tempList)
        #  else just append what is left without reversing
        else:
            for i in range(tempTrack):
                tempList.append(curr.value)
                curr = curr.next
            mainlist.extend(tempList)
            
    return mainlist
```
