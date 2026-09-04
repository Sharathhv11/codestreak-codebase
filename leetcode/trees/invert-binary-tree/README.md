# Invert Binary Tree

## Problem Information
- **Platform:** LeetCode
- **Concept / Pattern:** Trees
- **Language:** python3
- **Runtime:** 0 ms
- **Memory:** 19.4 MB
- **Tags:** None

## Complexity Analysis
- **Time Complexity:** O(N)
- **Space Complexity:** O(H)

## Explanation
The solution uses a recursive approach to traverse the binary tree. For each node, it recursively inverts its left and right subtrees, and then swaps the left and right children. The time complexity is O(N) because each node is visited once, and the space complexity is O(H) due to the recursion stack depth, where H is the height of the tree.

---
*Generated automatically by [CodeStreak](https://github.com/Sharathhv11/CodeStreak-webApp).*
