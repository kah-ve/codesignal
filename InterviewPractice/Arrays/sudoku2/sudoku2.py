def sudoku2(grid):
    checkList = list(map(lambda x: str(x), list(range(1, 10))))
    
    grid1 = []
    grid2 = []
    grid3 = []
    
    for k, i in enumerate(grid):
        for j in range(9):
            newList = [x for x in i if x == str(j+1)]           
            if len(newList) > 1:
                return False
            if (i[j] != ".") and (i[j] not in checkList):
                return False
        if k%3 == 2:
            grid1.extend(i[:3])
            grid2.extend(i[3:6])
            grid3.extend(i[6:9])
            for l in range(9):
                newList1 = [x for x in grid1 if x == str(l+1)]
                if len(newList1) > 1:
                    return False
                
                newList2 = [x for x in grid2 if x == str(l+1)]
                if len(newList2) > 1:
                    return False
                
                newList3 = [x for x in grid3 if x == str(l+1)]
                if len(newList3) > 1:
                    return False
        elif k%3!=0:
            grid1.extend(i[:3])
            grid2.extend(i[3:6])
            grid3.extend(i[6:9])
        else:
            grid1 = []
            grid2 = []
            grid3 = []    
            grid1.extend(i[:3])
            grid2.extend(i[3:6])
            grid3.extend(i[6:9])
                        
    for k, i in enumerate(list(zip(*grid))):
        for j in range(9):
            newList = [x for x in i if x == str(j+1)]            
            if len(newList) > 1:
                return False
            if (i[j] != ".") and (i[j] not in checkList):
                return False
        if k%3 == 2:
            grid1.extend(i[:3])
            grid2.extend(i[3:6])
            grid3.extend(i[6:9])
            for l in range(9):
                newList1 = [x for x in grid1 if x == str(l+1)]
                if len(newList1) > 1:
                    return False
                
                newList2 = [x for x in grid2 if x == str(l+1)]
                if len(newList2) > 1:
                    return False
                
                newList3 = [x for x in grid3 if x == str(l+1)]
                if len(newList3) > 1:
                    return False
        elif k%3!=0:
            grid1.extend(i[:3])
            grid2.extend(i[3:6])
            grid3.extend(i[6:9])
        else:
            grid1 = []
            grid2 = []
            grid3 = []    
            grid1.extend(i[:3])
            grid2.extend(i[3:6])
            grid3.extend(i[6:9])
            
    return True
                
grid = [
 [".","4",".",".",".",".",".",".","."], 
 [".",".","4",".",".",".",".",".","."], 
 [".",".",".","1",".",".","7",".","."], 
 [".",".",".",".",".",".",".",".","."], 
 [".",".",".","3",".",".",".","6","."], 
 [".",".",".",".",".","6",".","9","."], 
 [".",".",".",".","1",".",".",".","."], 
 [".",".",".",".",".",".","2",".","."], 
 [".",".",".","8",".",".",".",".","."]]
print (sudoku2(grid))
