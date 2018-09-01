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
    
        
