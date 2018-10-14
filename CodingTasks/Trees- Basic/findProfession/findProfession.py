def findProfession(level, pos):
    
    # if pos is odd then it will always be as the parent profession
    # if pos is even then it will be opposite of parent profession 
    # (this is true because E always makes E on left and similarly for D)
    # Also the pos of the child also determines parent. Level 3 Pos 3 for example has Parent at position ceil(3/2) = ceil(1.5) = 2
    
    E = "Engineer"
    D = "Doctor"
    
    if level == 1:
        return E
    
    if (findProfession(level-1, math.ceil(pos/2)) == D):
        return E if pos%2 == 0 else D

    return D if pos%2 == 0 else E

