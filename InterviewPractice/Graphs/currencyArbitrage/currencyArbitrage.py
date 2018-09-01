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
                    
        
        
