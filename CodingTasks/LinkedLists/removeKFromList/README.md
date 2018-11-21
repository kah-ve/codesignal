# Problem
Given a singly linked list of integers l and an integer k, remove all elements from list l that have a value equal to k.

Example

For 

    l = [3, 1, 2, 3, 4, 5] 
and 
    
    k = 3
the output should be

    removeKFromList(l, k) = [1, 2, 4, 5];
For 

    l = [1, 2, 3, 4, 5, 6, 7] 
and 

    k = 10
  
the output should be

    removeKFromList(l, k) = [1, 2, 3, 4, 5, 6, 7]

# Solution
```python
# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def removeKFromList(l, k):
    tempHead = ListNode(None)
    tempHead.next = l
    curr = tempHead
    
    while curr:
        while curr.next and curr.next.value == k:
            curr.next = curr.next.next
        curr = curr.next
    return tempHead.next
```
