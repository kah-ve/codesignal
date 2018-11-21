# Problem
Ratiorg got statues of different sizes as a present from CodeMaster for his birthday, each statue having an non-negative integer size. Since he likes to make things perfect, he wants to arrange them from smallest to largest so that each statue will be bigger than the previous one exactly by 1. He may need some additional statues to be able to accomplish that. Help him figure out the minimum number of additional statues needed.

Example

For `statues = [6, 2, 3, 8]`, the output should be
`makeArrayConsecutive2(statues) = 3.`
# Solution
```python
def makeArrayConsecutive2(statues):
    sortedStatues = sorted(statues)
    needed = 0    
    for i in range(len(sortedStatues)):
        current = sortedStatues[i]
        if i == len(sortedStatues)-1:
            break
        while(current + 1 != sortedStatues[i+1]):
            needed += 1
            current += 1
    return needed
```
