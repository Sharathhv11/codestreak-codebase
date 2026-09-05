# Diameter Of Binary Tree

## Problem Information
- **Platform:** LeetCode
- **Concept / Pattern:** Trees
- **Language:** python3
- **Runtime:** 4 ms
- **Memory:** 22.3 MB
- **Tags:** None

## Complexity Analysis
- **Time Complexity:** O(N)
- **Space Complexity:** O(H)

## Explanation
The solution uses a Depth First Search (DFS) approach to traverse the binary tree. For each node, it calculates the maximum depth of its left and right subtrees. The diameter passing through the current node is the sum of these depths, and this value is updated globally. The function returns the maximum depth from the current node to a leaf, which is used by its parent. The time complexity is O(N) as each node is visited once. The space complexity is O(H) due to the recursion stack, where H is the height of the tree.

---
*Generated automatically by [CodeStreak](https://github.com/Sharathhv11/CodeStreak-webApp).*
