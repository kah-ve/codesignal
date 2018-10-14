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

            
            
    
    
    
    
    
    
    
            
            
            

