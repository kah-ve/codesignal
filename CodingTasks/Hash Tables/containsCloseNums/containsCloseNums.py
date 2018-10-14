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
