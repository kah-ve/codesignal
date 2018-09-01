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
    
        
        
    
    

