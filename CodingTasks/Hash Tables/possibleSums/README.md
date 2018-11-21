# Problem
You have a collection of coins, and you know the values of the coins and the quantity of each type of coin in it. You want to know how many distinct sums you can make from non-empty groupings of these coins.

Example

For `coins = [10, 50, 100]` and `quantity = [1, 2, 1]`, the output should be
`possibleSums(coins, quantity) = 9.`

Here are all the possible sums:

    50 = 50;
    10 + 50 = 60;
    50 + 100 = 150;
    10 + 50 + 100 = 160;
    50 + 50 = 100;
    10 + 50 + 50 = 110;
    50 + 50 + 100 = 200;
    10 + 50 + 50 + 100 = 210;
    10 = 10;
    100 = 100;
    10 + 100 = 110.
    
As you can see, there are 9 distinct sums that can be created from non-empty groupings of your coins.

# Solution
```python
def possibleSums(coins, quantity):
    
    #  know the values of coins, and quantity of each type. Want to know distinct sums possible.
    #  if you have one coin, you have one possible distinct sum, when you add the second coin
    #  then you only need to check the coin itself, plus the coin plus its sum with the other 
    #  possible distinct sum. The distinct sums that come out of this are then new distinct sums...
    
    sums = set()
    for index, i in enumerate(coins):
        tempSet = set()
        for j in range(1, quantity[index]+1):
            #  add the number itself and any possible distinct sum of its additions with each other
            tempSum = j * i
            tempSet.add(tempSum) 
            
        #  run through the temp set above and the main set and check for distinct sum
        iterSum = set()
        for k in tempSet:
            for l in sums:
                iterSum.add(k + l)
    
        sums = sums.union(iterSum)
        sums = sums.union(tempSet)
    
    return len(sums)
```
