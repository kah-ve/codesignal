# Problem
Find the kth largest element in an unsorted array. This will be the kth largest element in sorted order, not the kth distinct element.

# Solution
```python
def kthLargestElement(nums, k):

    nums.sort(reverse=True)
    return nums[k-1]
```
