# Maximum Depth Of Binary Tree

## Problem Information
- **Platform:** LeetCode
- **Concept / Pattern:** DFS
- **Language:** python3
- **Runtime:** 7 ms
- **Memory:** 23 MB
- **Tags:** None

## Complexity Analysis
- **Time Complexity:** O(N)
- **Space Complexity:** O(H)

## Explanation
The solution uses Depth First Search (DFS) to traverse the binary tree. For each node, it recursively calculates the maximum depth of its left and right subtrees, adding 1 for the current node. The space complexity is determined by the maximum depth of the recursion stack, which is proportional to the height (H) of the tree.

---
*Generated automatically by [CodeStreak](https://github.com/Sharathhv11/CodeStreak-webApp).*
