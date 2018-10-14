def areFollowingPatterns(strings, patterns):

    patDict = {}
    stringSet = set()
    
    for i in range(len(strings)):
        if patterns[i] not in patDict:
            if strings[i] in stringSet:
                return False
            patDict[patterns[i]] = strings[i]
        else:
            if patDict[patterns[i]] != strings[i]:
                return False
        stringSet.add(strings[i])

    return True

        
