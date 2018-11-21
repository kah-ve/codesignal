# Problem
Given a string s, find and return the first instance of a non-repeating character in it. If there is no such character, return '_'.

Example

For s = "abacabad", the output should be
firstNotRepeatingCharacter(s) = 'c'.

# Solution
```python
def firstNotRepeatingCharacter(s):
    res = "_"
    d = {}
    for i,c in enumerate(s):
        if c in d.keys():
            d[c] = -1
        else:
            d[c] = i
    min_key = len(s)+1
    for k in d.keys():
        if d[k]>=0:
            min_key = min(min_key,d[k])
            res = s[min_key]
    return res
```
