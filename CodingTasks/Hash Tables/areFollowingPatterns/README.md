# Problem
Given an array strings, determine whether it follows the sequence given in the patterns array. In other words, there should be no i and j for which strings[i] = strings[j] and patterns[i] ≠ patterns[j] or for which strings[i] ≠ strings[j] and patterns[i] = patterns[j].

Example

For `strings = ["cat", "dog", "dog"]` and `patterns = ["a", "b", "b"]`, the output should be
`areFollowingPatterns(strings, patterns) = true;`

For `strings = ["cat", "dog", "doggy"]` and `patterns = ["a", "b", "b"]`, the output should be
`areFollowingPatterns(strings, patterns) = false.`

# Solution
```python
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
```
