https://app.codesignal.com/interview-practice/task/oZXs4td52fsdWC9kR
A tree is considered a binary search tree (BST) if for each of its nodes the following is true:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and the right subtrees must also be binary search trees.
Removing a value x from a BST t is done in the following way:

If there is no x in t, nothing happens;
Otherwise, let t' be a subtree of t such that t'.value = x.
If t' has a left subtree, remove the rightmost node from it and put it at the root of t';
Otherwise, remove the root of t' and its right subtree becomes the new t's root.

You're given a binary search tree t and an array of numbers queries. Your task is to remove queries[0], queries[1], etc., from t, step by step, following the algorithm above. Return the resulting BST.
