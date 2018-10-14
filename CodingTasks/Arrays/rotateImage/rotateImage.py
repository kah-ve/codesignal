def rotateImage(a):
    newArr = []
    for rows in list(zip(*a)):
        newArr.append(rows[::-1])
    return newArr
    
    
        

