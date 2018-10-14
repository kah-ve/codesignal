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
        
        

