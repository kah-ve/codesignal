def kthLargestElement(nums, k):

    nums.sort(reverse=True)
    return nums[k-1]
