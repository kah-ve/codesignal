# Problem
Given an array of integers, find the pair of adjacent elements that has the largest product and return that product.

Example:
For `inputArray = [3, 6, -2, -5, 7, 3]`, the output should be
`adjacentElementsProduct(inputArray) = 21`.

7 and 3 produce the largest product.
# Solution
```python
def adjacentElementsProduct(inputArray):
    curr_product = inputArray[0] * inputArray[1]
    for i in range(len(inputArray)-1):
        if inputArray[i] * inputArray[i+1] > curr_product:
            curr_product = inputArray[i] * inputArray[i+1]
    return curr_product
```
