# Balanced Binary Tree

## Problem Information
- **Platform:** LeetCode
- **Concept / Pattern:** Trees
- **Language:** python3
- **Runtime:** 0 ms
- **Memory:** 20.5 MB
- **Tags:** None

## Complexity Analysis
- **Time Complexity:** O(N)
- **Space Complexity:** O(H)

## Explanation
The solution uses a recursive Depth First Search (DFS) approach to traverse the binary tree. For each node, it calculates the height of its left and right subtrees. If the absolute difference in heights exceeds 1 at any node, the tree is unbalanced. The 'stop' flag is used for early termination. The time complexity is O(N) as each node is visited once, and space complexity is O(H) due to the recursion stack, where H is the height of the tree.

---
*Generated automatically by [CodeStreak](https://github.com/Sharathhv11/CodeStreak-webApp).*
