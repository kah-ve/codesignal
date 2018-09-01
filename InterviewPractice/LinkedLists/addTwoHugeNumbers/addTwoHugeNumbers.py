# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
from itertools import zip_longest

def addTwoHugeNumbers(a, b):

    output = []

    arrA = []
    arrB = []

    while a:
        arrA.append(a.value)
        a = a.next

    while b:
        arrB.append(b.value)
        b = b.next

    #  want to add the number together from the least significant digit since
    #  we need to carry the remainder

    arrA.reverse()
    arrB.reverse()

    carryOut = 0  # no starting carryOut
    for i, j in zip_longest(arrA, arrB, fillvalue=0):
        sum = i + j + carryOut  # add least significant two numbers along with carryOut
        toWrite = sum % 10000   # if sum < 10000 then will just append to output
        output.append(toWrite)  
        carryOut = sum // 10000  # if sum >= 10000 then carryOut = 1

    while carryOut:  # if carryOut at last sum then add a 1 to output (the end of the list)
        output.append(1)
        carryOut = 0

    output.reverse()
    return (output)
