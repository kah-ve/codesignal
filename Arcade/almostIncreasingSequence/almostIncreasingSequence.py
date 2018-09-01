def almostIncreasingSequence(sequence):
    
    check = 0
    check2 = 0
    for i in range(len(sequence)-1):
        n = sequence[i+1] - sequence[i]
        if n <= 0:
            check = check + 1
    
    for i in range(len(sequence)-2):
        n = sequence[i+2] - sequence[i]
        if n <= 0:
            check2 = check2 + 1
    
    if check > 1 or check2 > 1:
        return False
    else:
        return True
