# Binary Tree Inorder Traversal

## Problem Information
- **Platform:** LeetCode
- **Concept / Pattern:** Trees
- **Language:** python
- **Runtime:** 0 ms
- **Memory:** 12.2 MB
- **Tags:** None

## Complexity Analysis
- **Time Complexity:** O(N)
- **Space Complexity:** O(H)

## Explanation
The solution uses a recursive Depth First Search (DFS) approach to perform an inorder traversal of the binary tree. It visits the left subtree, then the current node, and finally the right subtree, appending node values to a list. The time complexity is O(N) as each node is visited once, and the space complexity is O(H) due to the recursion stack depth, where H is the height of the tree (worst case O(N) for a skewed tree, best case O(log N) for a balanced tree).

---
*Generated automatically by [CodeStreak](https://github.com/Sharathhv11/CodeStreak-webApp).*
