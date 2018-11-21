# Problem
You got sick because of walking in the woods at night, and have to spend a week at home without going out. Looking out of the window at the nearby woods you're wondering if there is anything you don't yet know about them. Suddenly you see a beautiful and very tall tree you haven't seen before. Since you have nothing to do, you decide to examine its structure and draw it in your notebook.

You became so exited about this new tree that your temperature went up, so you were forced to stay in bed. You can't see the tree from your bed, but luckily you have it drawn down. The first thing you'd like to find out about is the tree height. Looking at your drawing you suddenly realize that you forgot to mark the tree bottom and you don't know from which vertex you should start counting. Of course a tree height can be calculated as the length of the longest path in it (it is also called tree diameter). So, now you have a task you need to solve, so go ahead!

# Solution
```python
import sys
sys.setrecursionlimit(15000)
def treeDiameter(n, tree):
    print(sys.getrecursionlimit())
    g = Graph()
    for p in tree:
        g.add(p)
    v = g.find_diam()


    return max(0, v-1)
    


class Graph:
    def __init__(self):
        self.g = {}
    def add(self, p):
        self.g[p[0]] = self.g.get(p[0], []) + [p[1]]
        self.g[p[1]] = self.g.get(p[1], []) + [p[0]]
    def find_diam(self):
        if not self.g:
            return 0
        start = [k for k in self.g if len(self.g[k]) < 3][0]
        best = [0]
        h = self.height(start, None, best)
        return best[0]
    def height(self, start, parent, best):
        if start is None:
            return 0
        children = [self.height(c, start, best) for c in self.g[start] + [None] if c != parent]
        best[0] = max(1+sum(sorted(children, reverse=True)[:2]), best[0])
        #print(parent, start, best, 1+max(children))
        return 1+max(children)
        
    def __str__(self):
        return str(self.g) + ' ' + str(self.diam.items())
```
