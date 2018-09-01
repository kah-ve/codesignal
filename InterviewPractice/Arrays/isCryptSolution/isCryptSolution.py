def isCryptSolution(crypt, solution):
    #  convert solution to dict
    dictSol = {}
    for i in solution:
        dictSol[i[0]] = int(i[1])

    firstValue = 0
    secondValue = 0
    thirdValue = 0

    magnitude = len(crypt[0])
    magnitude = 10**(magnitude-1)
    for i in list(crypt[0]):
        firstValue += magnitude * dictSol[i]
        magnitude /= 10

    magnitude = len(crypt[1])
    magnitude = 10**(magnitude-1)
    for i in list(crypt[1]):
        secondValue += magnitude * dictSol[i]
        magnitude /= 10

    magnitude = len(crypt[2])
    magnitude = 10**(magnitude-1)
    for i in list(crypt[2]):
        thirdValue += magnitude * dictSol[i]
        magnitude /= 10

    #  can't start with a 0 (would've been more straightforward if I used string instead of int, but will try to make it work regardless)
    if (firstValue + secondValue == thirdValue):
        if (thirdValue != 0):
            if (dictSol[crypt[0][0]] == 0 and firstValue > 0):
                return False
            if (dictSol[crypt[1][0]] == 0 and secondValue > 0):
                return False
            if (dictSol[crypt[2][0]] == 0 and thirdValue > 0):
                return False

        if (thirdValue == 0):
            if (len(crypt[2]) > 1):
                return False

        if (secondValue == 0):
            if (len(crypt[1]) > 1):
                return False

        if (firstValue == 0):
            if (len(crypt[0]) > 1):
                return False

    if firstValue + secondValue == thirdValue:
        return True

    return False


crypt = ["SEND", "MORE", "MONEY"]
solution = [["O", "0"],
            ["M", "1"],
            ["Y", "2"],
            ["E", "5"],
            ["N", "6"],
            ["D", "7"],
            ["R", "8"],
            ["S", "9"]]

#  expected output true
result = isCryptSolution(crypt, solution)
print(result)

crypt2 = ["A", "A", "A"]
solution2 = [["A", "0"]]

#expected output true
result2 = isCryptSolution(crypt2, solution2)
print(result2)

crypt3 = ["AA", "AA", "AA"]
solution3 = [["A", "0"]]

#expected output false
result3 = isCryptSolution(crypt3, solution3)
print(result3)
