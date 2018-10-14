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
            
