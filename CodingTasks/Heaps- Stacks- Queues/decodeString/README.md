# Problem
Given an encoded string, return its corresponding decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is repeated exactly k times. Note: k is guaranteed to be a positive integer.

Note that your solution should have linear complexity because this is what you will be asked during an interview.
# Solution
```python
def decodeString(s):
    
    theStack = []
    
    #place the base string that will eventually be returned
    theStack.append([""])
    
    repeatNum = ""
    
    for char in s:
        if char.isdigit():
            repeatNum += char
        elif char == "[":
            theStack.append(["", int(repeatNum)])
            repeatNum = ""
        elif char == "]":
            string, repeat = theStack.pop()
            theStack[-1][0] += string * repeat
        else:
            theStack[-1][0] += char
    return theStack[-1][0]
```
