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
    

            
            
            
