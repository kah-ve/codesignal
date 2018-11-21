# Problem
Given an array of integers a, return a new array b using the following guidelines:

For each index i in b, the value of bi is the index of the aj nearest to ai and is also greater than ai.
If there are two options for bi, put the leftmost one in bi.
If there are no options for bi, put -1 in bi.
# Solution
```python
def nearestGreater(a):
    b = [None] * len(a) # initialize the return array
    stack = []
    
    for i in range(len(a)):
        
        while stack and a[stack[-1]] < a[i]:
            last_index = stack.pop()
            if b[last_index] == -1 or i - last_index < last_index - b[last_index]: 
            # b[last_index] can't be -1 since we made it through the while expression that checked if 
            # the element on the stack was less than the element on the right, so there is a 
            # nearestGreater element. Also check to see if the current index (in b) that is 
            # nearestGreater to b is closer than the one we just ran into (a[i]), if not then 
            # the new greater than element is switched to i
                b[last_index] = i
        if not stack:
            # if we have popped all the stack values and found no number that was greater than 
            # the a[i] element, then this is the newly found greatest element, leave it as -1
            b[i] = -1
        else:
            # stack is not empty and we have found a number that was greater than or equal to 
            # a[i] on the left. If it is greater then we can just insert that greater 
            # number's index into b
            if a[stack[-1]] > a[i]:
                b[i] = stack[-1]
            else:
                # the number a[stack[-1]] is not greater so it is equal, then it means that 
                # we want the closest greatest element that that number found on its left for now
                b[i] = b[stack[-1]]
        stack.append(i)
    return b
```
