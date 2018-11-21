# Problem
Sudoku is a number-placement puzzle. The objective is to fill a 9 × 9 grid with numbers in such a way that each column, each row, and each of the nine 3 × 3 sub-grids that compose the grid all contain all of the numbers from 1 to 9 one time.

Implement an algorithm that will check whether the given grid of numbers represents a valid Sudoku puzzle according to the layout rules described above. Note that the puzzle represented by grid does not have to be solvable.

Example

For

        grid = [  
                ['.', '.', '.', '1', '4', '.', '.', '2', '.'],  
                ['.', '.', '6', '.', '.', '.', '.', '.', '.'],  
                ['.', '.', '.', '.', '.', '.', '.', '.', '.'],  
                ['.', '.', '1', '.', '.', '.', '.', '.', '.'],  
                ['.', '6', '7', '.', '.', '.', '.', '.', '9'],  
                ['.', '.', '.', '.', '.', '.', '8', '1', '.'],  
                ['.', '3', '.', '.', '.', '.', '.', '.', '6'],  
                ['.', '.', '.', '.', '.', '7', '.', '.', '.'],  
                ['.', '.', '.', '5', '.', '.', '.', '7', '.']]  
the output should be

        sudoku2(grid) = true;

For

        grid = [  
                ['.', '.', '.', '.', '2', '.', '.', '9', '.'],  
                ['.', '.', '.', '.', '6', '.', '.', '.', '.'],  
                ['7', '1', '.', '.', '7', '5', '.', '.', '.'],  
                ['.', '7', '.', '.', '.', '.', '.', '.', '.'],  
                ['.', '.', '.', '.', '8', '3', '.', '.', '.'],  
                ['.', '.', '8', '.', '.', '7', '.', '6', '.'],  
                ['.', '.', '.', '.', '.', '2', '.', '.', '.'],  
                ['.', '1', '.', '2', '.', '.', '.', '.', '.'],  
                ['.', '2', '.', '.', '3', '.', '.', '.', '.']]  
the output should be

        sudoku2(grid) = false.
        
The given grid is not correct because there are two 1s in the second column. Each column, each row, and each 3 × 3 subgrid can only contain the numbers 1 through 9 one time.

# Solution
```python
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
```

