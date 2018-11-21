# Problem
Consider a special family of Engineers and Doctors. This family has the following rules:

Everybody has two children.
The first child of an Engineer is an Engineer and the second child is a Doctor.
The first child of a Doctor is a Doctor and the second child is an Engineer.
All generations of Doctors and Engineers start with an Engineer.
We can represent the situation using this diagram:

                E
           /         \
          E           D
        /   \        /  \
       E     D      D    E
      / \   / \    / \   / \
     E   D D   E  D   E E   D
Given the level and position of a person in the ancestor tree above, find the profession of the person.
Note: in this tree first child is considered as left child, second - as right.

# Solution
```python
def findProfession(level, pos):
    
    # if pos is odd then it will always be as the parent profession
    # if pos is even then it will be opposite of parent profession 
    # (this is true because E always makes E on left and similarly for D)
    # Also the pos of the child also determines parent. Level 3 Pos 3 for example has Parent at position ceil(3/2) = ceil(1.5) = 2
    
    E = "Engineer"
    D = "Doctor"
    
    if level == 1:
        return E
    
    if (findProfession(level-1, math.ceil(pos/2)) == D):
        return E if pos%2 == 0 else D

    return D if pos%2 == 0 else E
```
