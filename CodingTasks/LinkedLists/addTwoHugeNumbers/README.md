# Problem
You're given 2 huge integers represented by linked lists. Each linked list element is a number from 0 to 9999 that represents a number with exactly 4 digits. The represented number might have leading zeros. Your task is to add up these huge integers and return the result in the same format.

Example

For `a = [9876, 5432, 1999]` and `b = [1, 8001]`, the output should be
`addTwoHugeNumbers(a, b) = [9876, 5434, 0]`.

Explanation: 987654321999 + 18001 = 987654340000.

For `a = [123, 4, 5]` and `b = [100, 100, 100]`, the output should be
`addTwoHugeNumbers(a, b) = [223, 104, 105]`.

Explanation: 12300040005 + 10001000100 = 22301040105.

# Solution
```python
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
```
