# Problem
Given a singly linked list of integers l and a non-negative integer n, move the last n list nodes to the beginning of the linked list.

Example

For `l = [1, 2, 3, 4, 5]` and `n = 3`, the output should be
`rearrangeLastN(l, n) = [3, 4, 5, 1, 2];`

For `l = [1, 2, 3, 4, 5, 6, 7]` and `n = 1`, the output should be
`rearrangeLastN(l, n) = [7, 1, 2, 3, 4, 5, 6].`

# Solution
```python
# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def rearrangeLastN(l, n):
    
    
    arrList = []
    while (l):
        arrList.append(l.value)
        l = l.next
    
    arrList = arrList[-n:] + arrList[:-n]
    return arrList
```
