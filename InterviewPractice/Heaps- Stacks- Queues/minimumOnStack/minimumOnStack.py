def minimumOnStack(operations):
    
    stack = []
    result = []
    
    for operation in operations:
        if operation == "min":
            if stack:
                result.append(min(stack))
            continue
        elif operation == "pop":
            if stack:
                stack.pop()
            continue
        
        num = int(operation.split(" ")[1])
        stack.append(num)
    
    return result
        
        
        
        

