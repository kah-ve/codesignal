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
