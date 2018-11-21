# Problem
Implement a modified stack that, in addition to using push and pop operations, allows you to find the current minimum element in the stack by using a min operation.
# Solution
```python
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
```
