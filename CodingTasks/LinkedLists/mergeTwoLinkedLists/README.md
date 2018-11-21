# Problem
Given two singly linked lists sorted in non-decreasing order, your task is to merge them. In other words, return a singly linked list, also sorted in non-decreasing order, that contains the elements from both original lists.

Example

For `l1 = [1, 2, 3]` and `l2 = [4, 5, 6]`, the output should be
`mergeTwoLinkedLists(l1, l2) = [1, 2, 3, 4, 5, 6]`

For `l1 = [1, 1, 2, 4]` and `l2 = [0, 3, 5]`, the output should be
`mergeTwoLinkedLists(l1, l2) = [0, 1, 1, 2, 3, 4, 5]`

# Solution
```python
# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def mergeTwoLinkedLists(l1, l2):

    track1 = 0
    track2 = 0
    newlist = []
    
    currone = l1
    currtwo = l2
    
    while (currone or currtwo):
        if (currone):
            pass
        else:
            while (currtwo):
                newlist.append(currtwo.value)
                currtwo = currtwo.next
            break
        
        if (currtwo):
            pass
        else:
            while (currone):
                newlist.append(currone.value)
                currone = currone.next
            break
            
        if currone.value < currtwo.value:
            newlist.append(currone.value)
            currone = currone.next            
        elif currone.value == currtwo.value:
            newlist.append(currone.value)
            newlist.append(currtwo.value) # kind of unnecessary to call another list but makes it readable
            currone = currone.next
            currtwo = currtwo.next
        else:
            newlist.append(currtwo.value)
            currtwo = currtwo.next
            
        
    
    return newlist
```
