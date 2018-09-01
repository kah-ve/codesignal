def adjacentElementsProduct(inputArray):
    curr_product = inputArray[0] * inputArray[1]
    for i in range(len(inputArray)-1):
        if inputArray[i] * inputArray[i+1] > curr_product:
            curr_product = inputArray[i] * inputArray[i+1]
    return curr_product
