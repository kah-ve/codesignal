def checkPalindrome(inputString):
    wlen = len(inputString)
    half = wlen//2
    if wlen%2==0:        
        firstHalf = inputString[:half] #deed 0, 1 -- 2, 3, wlen/2 = 4/2 = 2 
        secondHalf = inputString[half:]
        secondHalf = secondHalf[::-1] #reverse
        if firstHalf == secondHalf:
            return True
    else:       
        firstHalf = inputString[:half] #catac 0, 1 -- 3, 4, wlen//2 = 2
        secondHalf = inputString[half + 1:]
        secondHalf = secondHalf[::-1]
        if firstHalf == secondHalf:
            return True
    return False
