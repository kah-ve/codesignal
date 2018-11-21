# Problem

Given an array of integers nums and an integer k, determine whether there are two distinct indices i and j in the array where nums[i] = nums[j] and the absolute difference between i and j is less than or equal to k.

Example

For `nums = [0, 1, 2, 3, 5, 2]` and `k = 3`, the output should be
`containsCloseNums(nums, k) = true.`

There are two 2s in nums, and the absolute difference between their positions is exactly 3.

For `nums = [0, 1, 2, 3, 5, 2]` and `k = 2`, the output should be
`containsCloseNums(nums, k) = false.`

The absolute difference between the positions of the two 2s is 3, which is more than k

# Solution
```python
def containsCloseNums(nums, k):
    theDict = {}    
    
    for i in range(len(nums)):
        if nums[i] not in theDict:
            theDict[nums[i]] = [i]
        else:
            theDict[nums[i]].append(i)
            for j in theDict[nums[i]]:
                if i - j <= k and i != j:
                    return True    
                      
            
    return False
```
