# Problem
Given an array a that contains only numbers in the range from 1 to a.length, find the first duplicate number for which the second occurrence has the minimal index. In other words, if there are more than 1 duplicated numbers, return the number for which the second occurrence has a smaller index than the second occurrence of the other number does. If there are no such elements, return -1.

Example

    For a = [2, 1, 3, 5, 3, 2], the output should be
    firstDuplicate(a) = 3.

# Solution
```python
def firstDuplicate(a):
    seen = set()
    duplicate = []
    
    for j, i in enumerate(a):
        if i not in seen:
            seen.add(i)
        else:
            duplicate.append([j, i])
    
    if len(duplicate) > 0:
        smaller = duplicate[0][0]      
        number = duplicate[0][1]
    else:
        return -1
    
    for i in duplicate:
        if i[0] < smaller:
            smaller = i[0]    
            number = i[1]
            
    return number
```
