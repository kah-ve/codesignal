# Problem
Given an array a composed of distinct elements, find the next larger element for each element of the array, i.e. the first element to the right that is greater than this element, in the order in which they appear in the array, and return the results as a new array of the same length. If an element does not have a larger element to its right, put -1 in the appropriate cell of the result array.
# Solution
```python
def nextLarger(a):

    stack = []
    
    returnArr = []
    
    #need to run through input arr backwards
    a.reverse()
    
    for num in a:
        while (stack and num > stack[-1]):
            stack.pop()
        if not stack:
            returnArr.append(-1)            
        else:
            returnArr.append(stack[-1])
        stack.append(num)
    
    # reverse back after using stack
    returnArr.reverse()
    return returnArr
```
