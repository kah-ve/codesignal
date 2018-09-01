def shapeArea(n):
    if n == 0:
        return 0
    area = 1
    for i in range(n):
        area += 4*i
    return area
        

