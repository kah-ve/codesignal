Since you became a director of a large company, you came to know all of your n employees perfectly well. You carefully studied their relationships and came up with a list of pairs of workers who respect one another. You are sure that in a healthy environment subordinates should respect their immediate superiors, which is why you would like to change the hierarchy in the company according to the list you composed. This hierarchy should be represented by a rooted tree, and for each pair of employees a, b, a is an immediate superior of b (or the other way round) if and only if a respects b and vice versa.

Given the number of people in you company n and the respectList you created, calculate the number of different hierarchies you can create.

Example

For n = 4 and respectList = [[0, 1], [1, 2], [2, 3], [3, 0], [1, 3]],
the output should be
hierarchiesCount(n, respectList) = 32.

Here are all possible hierarchies:

(0 -- 1), (1 -- 2), (2 -- 3);  
(1 -- 2), (2 -- 3), (3 -- 0);  
(2 -- 3), (3 -- 0), (0 -- 1);  
(3 -- 0), (0 -- 1), (1 -- 2);  
(1 -- 0), (1 -- 2), (1 -- 3);  
(3 -- 0), (3 -- 1), (3 -- 2);  
(1 -- 2), (1 -- 3), (3 -- 0);  
(1 -- 0), (1 -- 3), (3 -- 2).  

Each of them can be rooted at any of 4 employees, so the answer equals the number of hierarchies in the list above multiplied by 4.
