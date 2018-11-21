# Problem
Given a singly linked list of integers, determine whether or not it's a palindrome.

Example

For `l = [0, 1, 0]`, the output should be
`isListPalindrome(l) = true;`
For `l = [1, 2, 2, 3]`, the output should be
`isListPalindrome(l) = false.`

# Solution
```python
# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def isListPalindrome(l):
    arr = []
    curr = l
    while curr:
        arr.append(curr.value)
        curr = curr.next
    
    arrlen = len(arr)
    if arrlen%2==0:
        halfIndex = int(arrlen/2)
        firstHalf = arr[:halfIndex]
        secondHalf = arr[halfIndex:]
        secondHalf = secondHalf[::-1]
        if firstHalf == secondHalf:
            return True
    else:
        halfIndex = int(arrlen//2)
        firstHalf = arr[:halfIndex]
        secondHalf = arr[halfIndex+1:]
        secondHalf = secondHalf[::-1]
        if firstHalf == secondHalf:
            return True
    
    return False
```
