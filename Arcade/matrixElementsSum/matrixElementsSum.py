def matrixElementsSum(matrix):
    suitableRooms = 0
    zippedMatrix = list(zip(*matrix))
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            if zippedMatrix[i][j] == 0:
                break;
            else:
                suitableRooms += zippedMatrix[i][j]
    return suitableRooms
        
    

