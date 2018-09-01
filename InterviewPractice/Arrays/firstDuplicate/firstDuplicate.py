def firstDuplicate(a):
    seen = set()
    duplicate = []
    
    for j, i in enumerate(a):
        if i not in seen:
            seen.add(i)
        else:
            duplicate.append([j, i])
    
    if len(duplicate) > 0:
        smaller = duplicate[0][0]      
        number = duplicate[0][1]
    else:
        return -1
    
    for i in duplicate:
        if i[0] < smaller:
            smaller = i[0]    
            number = i[1]
            
    return number
    
