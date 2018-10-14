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
            

