Note: Try to solve this task in O(n3) time, where n is a number of currencies, since this is what you'll be asked to do during an interview.

A currency converter has the exchange rates exchange, such that exchange[i][j] represents the amount of money you would get for exchanging 1 unit of the ith currency for 1 unit of the jth currency. A "non-exchange" (that is, exchanging a currency with itself) is represented by exchange[i][i] = 1.

Write a function that returns True if it's possible to make money by doing a series of exchanges (i.e. to start with some currency C and to end with a greater amount of currency C after a series of exchanges), and False otherwise.

```python

def currencyArbitrage(exchange):
    
    N = len(exchange) # number of currencies to check
    
    for k in range(N):
        for i in range(N):
            for j in range(N):
                exchange[i][j] = max(exchange[i][j], exchange[i][k] * exchange[k][j])
                # iterate through each node and assign the new max of each currency exchange
                # to the max between the exchange from one node to another i -> j
                # or that node to an intermediary node than another node i -> k -> j
    
    for i in range(N):
        if exchange[i][i] > 1:
            # if a currency i -> i  has a value greater than 1, that means that a path was found
            # where arbitrage exists
            return True
    return False
    
```
