def makeArrayConsecutive2(statues):
    sortedStatues = sorted(statues)
    needed = 0    
    for i in range(len(sortedStatues)):
        current = sortedStatues[i]
        if i == len(sortedStatues)-1:
            break
        while(current + 1 != sortedStatues[i+1]):
            needed += 1
            current += 1
    return needed
            
    
